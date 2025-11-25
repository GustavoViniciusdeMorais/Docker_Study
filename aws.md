# AWS
### Install
```bash
python3 --version
apt install python3.10-venv -y
# Install with the bundler
# https://docs.aws.amazon.com/cli/v1/userguide/install-linux.html#install-linux-bundled
./awscli-bundle/install -i /usr/local/aws -b /usr/local/bin/aws
aws configure
# keys in the csv file _accessKeys.csv
# region must be us-east-1
# default output can be json
```
```bash
aws sts assume-role --role-arn arn:aws:iam::00000000000:role/gustavops --external-id ocupytheweb --role-session-name mysess
```
```bash
export AWS_ACCESS_KEY_ID=
export AWS_SECRETE_ACCESS_KEY=''
export AWS_SESSION_TOKEN=''

aws iam list-users
```
