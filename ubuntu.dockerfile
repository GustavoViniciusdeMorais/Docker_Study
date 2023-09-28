FROM ubuntu:jammy

RUN apt update

RUN apt install nano

RUN apt install curl -y

RUN apt update

RUN apt install systemctl -y

WORKDIR /var/www/html

ENTRYPOINT ["tail", "-f", "/dev/null"]