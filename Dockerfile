FROM python:3.7.5-slim

WORKDIR /usr/local/go
COPY ./ ./
RUN python -m pip install -r requirements.txt
RUN chmod +x main.py
RUN apt update
RUN apt install -y git
RUN import_data.sh