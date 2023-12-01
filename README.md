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
### Post degree lessons
- 1
    - DevOps three ways
    - Github actions with unit test
        - [Example](.github/workflows/first_job.yml)
- 2
    - Virtulization with OS proccesses and isolated fyle systems (Docker, DockerCompose, DockerSwarm)
        - [DockerCompose](docker-compose.yaml)
        - [DockerSwarm](DockerSwarm.md)
    - Infrastructure as Code (IaC with Terraform)
        - [Terraform](terraform.md)
            - [script example](main.tf)
