# My Docker Study

With Flask Python API

Gustavo

### Tutorials
- [Manual Mount Debian Container Runtime](./tutorials/ManualDebianContainerRuntime.md)

### Basic docker run and iteractive mode example
```bash
docker-compose up -d --build
docker exec -it -u 0 python_python_1 sh
python app.py
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
### Commands
```bash

docker-compose up -d --build

docker compose up -d --build [service_name]

docker compose down [service_name]

docker-compose down

docker exec -it [Container Name] bash

docker exec -it [Container Name] sh

docker ps

docker container ls

docker image ls

docker image pull alpine

docker container stop $(docker container ls -aq)

docker container rm $(docker container ls -aq)

docker image rm -f $(docker image ls -aq)

docker run -it -d -p 27017:27017 --expose=8080 --name=[Container Name] [Image Name]

docker run --rm -it [Container Name] /bin/sh

docker run --rm -it [Container Name] bash

docker network rm $(docker network ls -q)

```

### Push to docker hub
```bash
docker commit CONTAINER_ID  CONTAINER_NAME:TAG

docker login # user and pass of dockerhub

docker tag <name-of-image>:<tag> <hub-user>/<repo-name>:<tag>
docker push <hub-user>/<repo-name>:<tag>
```
### Use external network inside other docker compose file
```yaml
services:
    nginx:
        build:
            context: .
            dockerfile: ubuntu.dockerfile
        ports:
            - 83:80
        volumes:
            - ./:/var/www/html
        container_name: gusphp
        # depends_on:
        #     - mysql
        #     - mailhog_yii
        networks:
            other_network:
              ipv4_address: 10.171.0.17
networks:
  other_network:
    external: true
```
