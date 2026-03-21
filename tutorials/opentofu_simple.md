## 1. Install OpenTofu on Debian

```bash
# Install dependencies
sudo apt-get update
sudo apt-get install -y apt-transport-https ca-certificates curl gnupg

sudo install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://get.opentofu.org/opentofu.gpg | sudo tee /etc/apt/keyrings/opentofu.gpg >/dev/null
curl -fsSL https://packages.opentofu.org/opentofu/tofu/gpgkey | sudo gpg --no-tty --batch --dearmor -o /etc/apt/keyrings/opentofu-repo.gpg >/dev/null
sudo chmod a+r /etc/apt/keyrings/opentofu.gpg /etc/apt/keyrings/opentofu-repo.gpg

echo \
  "deb [signed-by=/etc/apt/keyrings/opentofu.gpg,/etc/apt/keyrings/opentofu-repo.gpg] https://packages.opentofu.org/opentofu/tofu/any/ any main
deb-src [signed-by=/etc/apt/keyrings/opentofu.gpg,/etc/apt/keyrings/opentofu-repo.gpg] https://packages.opentofu.org/opentofu/tofu/any/ any main" | \
  sudo tee /etc/apt/sources.list.d/opentofu.list > /dev/null
sudo chmod a+r /etc/apt/sources.list.d/opentofu.list

sudo apt-get update
sudo apt-get install -y tofu
```

## 2. Create OpenTofu Configuration File

Create a file named `main.tf`:

```hcl
terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0"
    }
  }
}

provider "docker" {
  host = "unix:///var/run/docker.sock"
}

resource "docker_image" "nginx" {
  name = "nginx:latest"
  keep_locally = false
}

resource "docker_container" "nginx" {
  name  = "simple-nginx"
  image = docker_image.nginx.name
  ports {
    internal = 80
    external = 8080
  }
}
```

## 3. Apply the Configuration

```bash
cd tofus

# Initialize OpenTofu (downloads Docker provider)
tofu init

# See what will be created
tofu plan

# Create the Docker container
tofu apply -auto-approve
```

## 4. Verify It Works

```bash
# Check if container is running
docker ps

# Test nginx is responding
curl http://localhost:8080
```

## 5. Clean Up (Optional)

```bash
# Remove the container and image
tofu destroy -auto-approve
```
