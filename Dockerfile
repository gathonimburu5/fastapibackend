FROM python:3.11-slim

WORKDIR /employee

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .