FROM python:alpine3.7


RUN apk update
RUN apk add --virtual deps gcc python-dev linux-headers musl-dev postgresql-dev
RUN apk add --no-cache libpq

#COPY start.sh /start.sh
COPY . ./djangoapp
WORKDIR ./djangoapp

RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip install -r requirements.txt

RUN apk del deps

RUN python manage.py migrate
RUN python manage.py collectstatic
