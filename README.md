# Devops Course

### Basic docker commands
```bash
docker compose up -d --build ubuntu
```
### Expose ports
```bash
# It is always local to container, even in docker compose file
docker run -d -p HOST_PORT:CONTAINER_PORT nginx
```
### Pull and run
```bash
docker pull kalilinux/kali-rolling
docker run <options> <image_ID>
docker run -d --name kalilinux -p 83:8080 kalilinux/kali-rolling
```
### Format docker ps output
```bash
docker ps --format "{{.ID}}: {{.Names}}"
```
