FROM python:3.7-alpine
LABEL MAINTAINER Nitish Kumar Mahto

ENV PYTHONBUFFERED 1

COPY ./requirements.txt /requirements.txt

RUN apk add --update --no-cache postgresql-client
RUN apk add --update --no-cache --virtual .tmp-build-deps \
    gcc linux-headers postgresql-dev libc-dev

RUN pip install -r /requirements.txt
RUN apk del .tmp-build-deps
RUN mkdir /app
WORKDIR /app
COPY ./app /app
RUN adduser -D nitish
USER nitish
