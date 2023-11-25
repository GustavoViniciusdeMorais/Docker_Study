# Devops Studies

Created by: Gustavo Morais

### Test python flask API example
```sh
docker-compose up -d --build
docker exec -it -u 0 python_python_1 sh
python app.py
```

### Build container to make requests
```sh
sudo curl -X GET http://localhost
```
Inside of python.dockerfile add the followin code <br>
This code will enable to request a simple python API when container starts
```yaml
FROM gustavovinicius/guspy:flaskmarshmallow

WORKDIR /var/www/html

ENTRYPOINT ["tail", "-f", "/dev/null"]

ENTRYPOINT [ "python3" ]
CMD [ "app.py" ]
```
