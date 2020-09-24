FROM python:3.7.5-slim

WORKDIR /usr/local/go
COPY ./ ./
RUN apt-get update
RUN apt-get -y install wget
RUN apt-get -y install unzip
RUN chmod a+x import_data.sh
RUN chmod +x tests.py
RUN ./import_data.sh