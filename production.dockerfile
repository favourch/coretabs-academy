FROM python:alpine3.7

RUN apk update
RUN apk upgrade
RUN apk add --virtual deps gcc python-dev linux-headers musl-dev postgresql-dev
RUN apk add --no-cache libpq
RUN apk add jpeg-dev \
    zlib-dev \
    freetype-dev \
    lcms2-dev \
    openjpeg-dev \
    tiff-dev \
    tk-dev \
    tcl-dev \
    harfbuzz-dev \
    fribidi-dev
#RUN apk add --no-cache bash
#RUN rm /bin/sh && ln -s /bin/bash /bin/sh


COPY . ./djangoapp
WORKDIR ./djangoapp

#RUN pip install --upgrade pip
#RUN pip install --upgrade setuptools

#RUN pip install virtualenv
#RUN virtualenv venv
#RUN source ./venv/bin/activate

#RUN pip install -r requirements.txt

#RUN source ./venv/bin/activate

RUN apk del deps

RUN echo "" >> ./coretabs/settings.py
RUN echo "from coretabs.deploy_settings import *" >> ./coretabs/settings.py

#RUN python manage.py collectstatic
#RUN python manage.py migrate
#RUN echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'admin')" | python manage.py shell

CMD [ "sh", "-c", "source ./venv/bin/activate && gunicorn --bind 0.0.0.0:8000 coretabs.wsgi" ]
#CMD ["./build.sh"]
