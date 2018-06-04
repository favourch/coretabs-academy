FROM python:alpine3.7

WORKDIR ./djangoapp

RUN python manage.py migrate