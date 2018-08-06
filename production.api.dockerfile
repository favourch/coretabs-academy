FROM python:alpine3.7

# Install libraries

RUN apk update
RUN apk upgrade
RUN apk add memcached
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



#RUN PATH=$PATH:/opt/local/lib/postgresql91/bin/

# Copy from current folder

COPY ./src/ ./djangoapp
WORKDIR ./djangoapp

# Intall dependencies 

RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip install -r requirements.txt

RUN apk del deps

RUN python manage.py collectstatic
