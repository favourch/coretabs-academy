FROM python:alpine3.7


COPY . ./djangoapp
WORKDIR ./djangoapp

RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip install -r requirements.txt

RUN python manage.py migrate
RUN python manage.py collectstatic

RUN echo from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'admin') | python manage.py shell
RUN echo from django.contrib.sites.models import Site; Site.objects.create(name='localhost', domain='127.0.0.1:8000') | python manage.py shell

RUN gunicorn --bind 0.0.0.0:8000 wsgi.py