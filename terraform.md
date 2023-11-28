# Terraform Study

```sh
```

- [Terraform Install](https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli)
- 

### Install
```sh
sudo apt-get update && sudo apt-get install -y gnupg software-properties-common

wget -O- https://apt.releases.hashicorp.com/gpg | \
gpg --dearmor | \
sudo tee /usr/share/keyrings/hashicorp-archive-keyring.gpg

gpg --no-default-keyring \
--keyring /usr/share/keyrings/hashicorp-archive-keyring.gpg \
--fingerprint

echo "deb [signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] \
https://apt.releases.hashicorp.com $(lsb_release -cs) main" | \
sudo tee /etc/apt/sources.list.d/hashicorp.list


sudo apt update

sudo apt-get install terraform

terraform --help
```

### Simple tutorial
Write file main.tf
```sh
sudo terraform init

sudo terraform apply // type yes

sudo docker ps // check container tutorial is running

http://localhost:8000/ nginx page

sudo terraform destroy // destroy terraform

sudo docker ps // container is not running
```