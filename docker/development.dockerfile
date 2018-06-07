FROM python:alpine3.7

WORKDIR ./djangoapp

CMD ["python manage.py migrate", "python manage.py runserver"]