FROM python:alpine3.7


COPY . ./djangoapp
WORKDIR ./djangoapp

RUN pip install --upgrade setuptools
#RUN pip install virtualenv
#RUN virtualenv venv
#RUN source ./venv/bin/activate
RUN pip install -r requirements.txt

RUN python manage.py migrate