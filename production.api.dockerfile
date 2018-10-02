FROM coretabsacademy/academy_api_base

# Copy source code
COPY ./src/api/ /var/djangoapp
WORKDIR /var/djangoapp

# Clean up
RUN apk del deps

# Collect static files
RUN mkdir static
RUN python manage.py collectstatic
