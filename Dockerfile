FROM python:3.10.0-alpine

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /code

COPY requirements.txt /code/

COPY django.sh /code/

RUN pip install -r requirements.txt

COPY . /code/
