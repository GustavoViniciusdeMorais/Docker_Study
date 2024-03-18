 #!/bin/bash
cat /etc/group | grep docker
sudo groupadd docker
sudo usermod -aG docker $USER
newgrp docker
sudo systemctl restart docker