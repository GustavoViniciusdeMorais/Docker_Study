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

### Config docker group
```sh
sudo chmod u+x addUserToDockerGroup.sh
sudo ./addUserToDockerGroup.sh
```

### minikube
```sh
sudo minikube start --force
sudo minikube stop --force
```

### Start dashboard
```sh
sudo minikube dashboard
```

### Create namespaces
```sh
sudo kubectl apply -f namespaces.yaml
sudo kubectl get namespaces
```

### Create nginx pod at dev env
```sh
sudo kubectl apply -f deployDevelopment.yaml
```
