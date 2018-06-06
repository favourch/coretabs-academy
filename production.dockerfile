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

RUN echo "from coretabs.deploy_settings import *" >> ./coretabs/settings.py

#RUN python manage.py migrate
CMD python manage.py collectstatic



CMD python manage.py migrate
CMD echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'admin')" | python manage.py shell
#CMD echo "from django.contrib.sites.models import Site; Site.objects.create(name='localhost', domain='127.0.0.1:8000')" | python manage.py shell

CMD gunicorn --bind 0.0.0.0:8000 coretabs.wsgi