# syntax=docker/dockerfile:1

FROM python:alpine
WORKDIR .
COPY requirments.txt requirments.txt
RUN pip3 install -r requirments.txt
COPY . .
CMD gunicorn --bind 0.0.0.0:3000 wsgi:app

MAINTAINER moodyomarz "contact@devmoody.com"
