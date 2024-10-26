# API Example

Created by Gustavo Morais

### 
```sh
```

### Minikube
```sh
sudo minikube start --force
sudo minikube stop --force
```

### Create env
```sh
kubectl apply -f src/kubernete/persistent-volume.yaml
kubectl apply -f src/kubernete/redis-deployment.yaml
kubectl apply -f src/kubernete/api-deployment.yaml
```

### Access python API
```sh
kubectl get pods
kubectl exec -it <python-api-pod-name> -- /bin/sh
pip install flask redis
flask run --host=0.0.0.0 --port=5000
```

### Test
```sh
curl http://<EXTERNAL-IP>/set/mykey/myvalue
curl http://<EXTERNAL-IP>/get/mykey
```
