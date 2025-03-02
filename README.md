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
minikube start --force
minikube stop --force
```

### infos
```sh
kubectl get nodes
kubectl cluster-info
```

### Start dashboard
```sh
minikube dashboard
```

### Create namespaces
```sh
kubectl apply -f namespaces.yaml
kubectl get namespaces
```

### Create nginx pod at dev env
```sh
kubectl apply -f deployDevelopment.yaml
```

### List deployments
```sh
kubectl get deployments -n development
```

### List the pods
```sh
kubectl get pods -n development
```

### List pods with extra info to see the pod IP address
```sh
kubectl get pods -n development -o wide
```

### Delete pod
```sh
kubectl delete pod [pod_name] -n development
```

### List pod events and infos
```sh
kubectl describe pod [pod_name] -n development
```

### Create busybox pod to test if other pods are running with wget
```sh
kubectl apply -f busybox.yaml
kubectl exec -it busybox-574654f4cb-mdcrx -- /bin/sh
wget [other-pod-IP]
cat index.html // list the wget result from other pode response
```

### Check the logs of the nginx pod
```sh
kubectl logs myapp-596cc748d4-4wx9c -n development
```

### Expose the app in the localhost
```sh
minikube tunnel // creates the link between the pod and the service
kubectl apply -f service.yaml
kubectl get services -n development // get the external IP of the service to curl
curl [external-IP]
```

### Simple env cleaning (delete everything)
```sh
kubectl delete -f service.yaml
kubectl delete -f busybox.yaml
kubectl delete -f deployDevelopment.yaml
kubectl delete -f namespaces.yaml
minikube delete
```

### Delete service, pods, and stop minikube
```sh
kubectl delete service [service-name] -n development
kubectl scale deployment myapp --replicas=0 -n development // scale pods to zero, no pods
kubectl scale deployment busybox --replicas=0 -n default
minikube stop
```
