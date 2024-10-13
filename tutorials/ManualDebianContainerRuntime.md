# Manual Mount Debian Container Runtime
Here’s a simple step-by-step guide for mounting a directory, unsharing namespaces, creating a chroot, setting up control groups (cgroups), applying Linux capabilities, and running an application within the namespace on Debian Linux.

### 1. Mount a Directory

We will mount a directory to serve as the root of our chroot jail.

```bash
# Create a directory to use as the new root for the chroot
sudo mkdir /mnt/my_root

# Mount a tmpfs to simulate the isolation (temporary filesystem)
sudo mount -t tmpfs none /mnt/my_root
```

### 2. Unshare Namespace

Unsharing a namespace isolates the current process from the host system. We can unshare a few namespaces: `mount`, `UTS`, `IPC`, and `PID`. Let’s unshare `mount` and `PID` for this example:

```bash
# Unshare the mount and PID namespaces
sudo unshare --mount --pid --fork --mount-proc bash
```

This command opens a new shell in an isolated mount and PID namespace.

### 3. Create a Chroot

Now, we create a chroot environment. A chroot changes the root directory for the current process and its children.

```bash
# Create a minimal root environment in the /mnt/my_root directory
sudo mkdir -p /mnt/my_root/{bin,lib,lib64}

# Copy bash and its dependencies to the new root
sudo cp /bin/bash /mnt/my_root/bin
sudo cp -a /lib/x86_64-linux-gnu /mnt/my_root/lib
sudo cp -a /lib64 /mnt/my_root/lib64
```

Now, change the root of the shell:

```bash
# Enter the chroot environment
sudo chroot /mnt/my_root /bin/bash
```

You are now inside the new root (chrooted).

### 4. Create and Bind Control Groups (cgroups)

Control groups help manage and limit the resources (CPU, memory, etc.) used by the processes. Here’s a simple example to bind a PID to a cgroup.

```bash
# Create a control group directory
sudo mkdir -p /sys/fs/cgroup/my_cgroup

# Limit the CPU usage for this group (optional)
echo "50000" | sudo tee /sys/fs/cgroup/my_cgroup/cpu.cfs_quota_us

# Bind a process (e.g., PID 1 from the unshared PID namespace) to this group
echo $$ | sudo tee /sys/fs/cgroup/my_cgroup/cgroup.procs
```

This binds the current process (with the PID $$) to the control group.

### 5. Set Linux Capabilities on the Chroot

You can set capabilities for processes in the chroot using `setcap`. Capabilities allow for fine-grained control over what a process can do without giving full root privileges.

```bash
# Install the libcap2-bin package if not already installed
sudo apt-get install libcap2-bin

# Set capabilities on a binary inside the chroot (e.g., allow network access)
sudo setcap cap_net_raw,cap_net_admin+p /mnt/my_root/bin/bash
```

### 6. Run a Simple Application in the Namespace

Now that everything is set up, you can run an application inside the isolated namespace.

```bash
# In the chroot environment, run a simple application (e.g., bash)
exec /bin/bash
```

You can also run a simple network-related application to test the capabilities:

```bash
# In the chrooted shell, you can now run a network command (ping)
ping google.com
```

### 7. Reverting the Changes

After you are done, you can revert the changes as follows:

1. **Exit the Chroot and Namespace**:

   ```bash
   exit # Exit from the chrooted bash
   exit # Exit from the unshared namespace shell
   ```

2. **Unmount the Directory**:

   ```bash
   sudo umount /mnt/my_root
   ```

3. **Remove the Control Group**:

   ```bash
   sudo rmdir /sys/fs/cgroup/my_cgroup
   ```

4. **Remove the Chroot Directory**:

   ```bash
   sudo rm -rf /mnt/my_root
   ```

This will clean up all the changes made during the process.