# Magic Test

## Coding Challenges

### Setup

Build image from Dockerfile with docker

```bash
docker build --tag magic:1.0 .
```

Run docker container from image

```bash
docker run -it  --name mag magic:1.0 /bin/bash
```

Run tests inside docker container

```bash
python -m tests
```

Run flatten array function

```bash
python main.py flatten_array -a [[1,2,[3]],4]
```

Run temperatures function for lowest temperatures

```bash
python main.py temperatures -f data.csv -fn lowest
```

Run temperatures function for lowest temperatures

```bash
python main.py temperatures -f data.csv -fn lf_dates -r '[2000.000, 2002.000]'
```