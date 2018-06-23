#!/bin/sh

echo "Migrating db and collecting statics"
docker exec -it coretabs_academy_django_api sh -c "source ./venv/bin/activate && python manage.py migrate && python manage.py collectstatic"

docker exec -it coretabs_academy_django_api sh -c "source ./venv/bin/activate && echo ""from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'admin')"" | python manage.py shell"

read -p "Enter SECRET_KEY: " secret_key
export SECRET_KEY=$secret_key

read -p "Enter DATABASE_URL: " database_url
export DATABASE_URL=$database_url

# Email env vars

read -p "Enter EMAIL_HOST: " email_host
export EMAIL_HOST=$email_host

read -p "Enter EMAIL_HOST_USER: " email_host_user
export EMAIL_HOST_USER=$email_host_user

read -p "Enter EMAIL_HOST_PASSWORD: " email_host_password
export EMAIL_HOST_PASSWORD=$email_host_password

read -p "Enter ADMIN_EMAILS: " admin_emails
export ADMIN_EMAILS=$admin_emails

# Discourse env vars

read -p "Enter DISCOURSE_HOST: " discourse_host
export DISCOURSE_HOST=$discourse_host

read -p "Enter DISCOURSE_SSO_SECRET: " discourse_sso_secret
export DISCOURSE_SSO_SECRET=$discourse_sso_secret

read -p "Enter DISCOURSE_API_KEY: " discourse_api_key
export DISCOURSE_API_KEY=$discourse_api_key

read -p "Enter DISCOURSE_API_USERNAME: " discourse_api_username
export DISCOURSE_API_USERNAME=$discourse_api_username

# Sentry env vars

read -p "Enter SENTRY_DSN: " sentry_dns
export SENTRY_DSN=$sentry_dns


#echo "Running: collectpython manage.py collectstaticstatic"
#exec python manage.py collectstatic

#echo "Creating super user"
#echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'admin')" | python manage.py shell"