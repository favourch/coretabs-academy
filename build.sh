#!/bin/sh

echo "Migrating db and collecting statics"
docker exec -it coretabs_academy_django_api sh -c "source ./venv/bin/activate && python manage.py migrate && python manage.py collectstatic"

docker exec -it coretabs_academy_django_api sh -c "source ./venv/bin/activate && echo ""from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'admin')"" | python manage.py shell"

#echo "Running: collectpython manage.py collectstaticstatic"
#exec python manage.py collectstatic

#echo "Creating super user"
#echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'admin')" | python manage.py shell"