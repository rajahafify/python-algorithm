FROM python:3.5-alpine

RUN mkdir /app
WORKDIR /app

COPY . /app

CMD python algorithms/selection-sort.py
