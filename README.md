# Basic Credit Card

## Setup
run `chmod a+x import_data.sh`

run `./import_data.sh`

Build image from Dockerfile with docker

```bash
docker build --tag magic:1.0 .
```

Run docker container from image

```bash
docker run -it  --name bcc magic:1.0 /bin/bash
```

Run tests inside docker container

```bash
python tests
```