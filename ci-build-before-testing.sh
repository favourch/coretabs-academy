apk update
apk upgrade
apk add memcached
apk add --virtual build-deps gcc python3-dev musl-dev
apk add --no-cache py3-virtualenv postgresql-dev nodejs nodejs-npm jpeg-dev
apk add --no-cache zlib-dev freetype-dev lcms2-dev openjpeg-dev tiff-dev tk-dev tcl-dev harfbuzz-dev fribidi-dev
apk add --virtual deps gcc python-dev linux-headers musl-dev postgresql-dev
apk add --no-cache libpq
apk add jpeg-dev \
    zlib-dev \
    freetype-dev \
    lcms2-dev \
    openjpeg-dev \
    tiff-dev \
    tk-dev \
    tcl-dev \
    harfbuzz-dev \
    fribidi-dev \
    libcurl \
    libressl-dev

# Needed for pycurl
export PYCURL_SSL_LIBRARY=openssl

# Install packages only needed for building, install and clean on a single layer
apk add --no-cache --virtual .build-dependencies build-base curl-dev \
    && pip install pycurl \

virtualenv venv
source ./venv/bin/activate
pip install -r ./src/requirements.txt
apk del build-deps
apk del .build-dependencies
python ./src/manage.py migrate
python ./src/manage.py populate 10 4 3 2
npm i newman -g
python ./src/manage.py runserver &
