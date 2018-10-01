FROM python:3.6.6-alpine3.8 as base

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
    fribidi-dev \
    libcurl

# Needed for pycurl
ENV PYCURL_SSL_LIBRARY=openssl

# Install packages only needed for building, install and clean on a single layer
RUN apk add --no-cache --virtual .build-dependencies build-base curl-dev \
    && pip install pycurl \
    && apk del .build-dependencies

# Copy requirements
COPY ./src/requirements.txt ./djangoapp/requirements.txt
WORKDIR ./djangoapp

# Intall dependencies 
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip install -r requirements.txt

# Dependencies ready, now let's copy the source code
FROM base

# Copy source code
COPY ./src/ ./djangoapp
WORKDIR ./djangoapp

# Clean up
RUN apk del deps

# Collect static files
RUN mkdir static
RUN python manage.py collectstatic
