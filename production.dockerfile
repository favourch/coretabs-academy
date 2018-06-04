FROM python:alpine3.7


COPY . ./djangoapp
WORKDIR ./djangoapp

RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip install -r requirements.txt

RUN python manage.py migrate