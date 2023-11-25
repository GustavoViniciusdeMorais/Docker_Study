# Docker Swarm

```sh
```

### Config python env
Inside of python.dockerfile add the followin code <br>
This code will enable to request a simple python API when container starts
```yaml
FROM gustavovinicius/guspy:flaskmarshmallow

WORKDIR /var/www/html

ENTRYPOINT ["tail", "-f", "/dev/null"]

ENTRYPOINT [ "python3" ]
CMD [ "app.py" ]
```
```sh
sudo curl -X GET http://localhost
```

### Swarm commands
Star the swarm
```sh
docker swarm init --advertise-addr 127.0.0.1
```
You can join any machines to the swarm to have redundancy
```sh
docker swarm join --token SWMTKN-1-036k9xevg9ej3v61ujv8uhhmf59eziaty29mbi6goj3lqicbru-3seet5ywq0xguxirxyg13rg1g 127.0.0.1:2377
```
A service allows you to instantiate containers inside a swarm <br>
```sh
docker service create --name [swarm name] --replicas [number] --publish [local port]:[service port] [container image name]
```
Example <br>
User docker image ls to search for an image
```sh
docker service create --name python-api --replicas 3 --publish 8080:80 docker_study_pydevops
```
List the services
```sh
docker service ls
```
Stop a container an see if the service is gona make another to replace it
```sh
docker stop [container id]
```
Remove service
```sh
docker service rm
```