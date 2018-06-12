call venv\scripts\activate.bat
echo from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', '8520asdf') | python manage.py shell
pause