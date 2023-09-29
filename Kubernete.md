# Kubernete

Created by Gustavo Morais

```sh
```

### At the docker service configuration, add the attribute
```
cap_add:
  - ALL
```
Example
```
services:
    ubuntu:
        build:
            context: .
            dockerfile: ubuntu.dockerfile
        container_name: stddocker
        ports:
            - 80:8000
        volumes:
            - ./:/var/www/html
        cap_add:
            - ALL
        networks:
            stddocker-app-network:
                ipv4_address: 11.0.0.8
```

### Install docker
```sh
chmod u+x installDocker.sh
./installDocker.sh
```

### install kubectl and minikube
```sh
chmod u+x installMinikube.sh
./installMinikube.sh
```

### minikube
```sh
minikube start --force
minikube stop --force
```
