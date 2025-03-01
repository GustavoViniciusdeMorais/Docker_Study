# My Docker Study

With Flask Python API

Gustavo

### Tutorials
- [Manual Mount Debian Container Runtime](./tutorials/ManualDebianContainerRuntime.md)

### Basic docker run and iteractive mode example
```
docker-compose up -d --build
docker exec -it -u 0 python_python_1 sh
python app.py
```

### Pull and run
```
docker pull kalilinux/kali-rolling
docker run <options> <image_ID>
```

### Commands
```

docker-compose up -d --build

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
```
docker commit CONTAINER_ID  CONTAINER_NAME:TAG

docker login # user and pass of dockerhub

docker tag <name-of-image>:<tag> <hub-user>/<repo-name>:<tag>
docker push <hub-user>/<repo-name>:<tag>
```
