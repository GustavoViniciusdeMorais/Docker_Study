# Export docker images as files
```bash
docker image ls | grep hacking
mkdir images
docker save -o images/parrot_2.tar hacking_studies-parrot:latest
```
### Load image
```bash
docker load --input images/parrot_2.tar
```
