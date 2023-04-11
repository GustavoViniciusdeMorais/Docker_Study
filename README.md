# My Docker Study

With Flask Python API

Gustavo

```
docker-compose up -d --build
docker exec -it -u 0 python_python_1 sh
python app.py
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
