# Generated by Django 2.0.4 on 2019-03-17 20:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('full_name', models.CharField(max_length=126, verbose_name='full name')),
                ('date', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='CertificateSignature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=126)),
                ('photo', models.ImageField(upload_to='signatures/')),
            ],
        ),
        migrations.CreateModel(
            name='CertificateTemplate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=126)),
                ('body', models.CharField(max_length=512)),
                ('signature', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='profiles.CertificateSignature')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('0', 'Student'), ('1', 'Mentor'), ('2', 'Tutor'), ('3', 'Admin')], default='0', max_length=10)),
                ('level', models.CharField(choices=[('0', 'Beginner'), ('1', 'Intermediate'), ('2', 'Advanced')], default='0', max_length=10)),
                ('description', models.CharField(blank=True, max_length=50)),
                ('country', models.CharField(blank=True, choices=[('', ''), ('DZ', 'Algeria'), ('TN', 'Tunisia')], max_length=50)),
                ('bio', models.CharField(blank=True, max_length=1000)),
                ('languages', models.CharField(blank=True, max_length=100)),
                ('facebook_link', models.CharField(blank=True, max_length=100)),
                ('twitter_link', models.CharField(blank=True, max_length=100)),
                ('linkedin_link', models.CharField(blank=True, max_length=100)),
                ('website_link', models.CharField(blank=True, max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='certificate',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='certificates', to='profiles.Profile'),
        ),
        migrations.AddField(
            model_name='certificate',
            name='template',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.CertificateTemplate'),
        ),
    ]
