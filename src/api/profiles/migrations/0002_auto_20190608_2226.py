# Generated by Django 2.0.9 on 2019-06-08 19:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=500)),
                ('photo', models.ImageField(blank=True, upload_to='projects')),
                ('github_link', models.CharField(blank=True, max_length=100)),
                ('live_demo_link', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='languages',
            new_name='skills',
        ),
        migrations.AddField(
            model_name='profile',
            name='github_link',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='profile',
            name='country',
            field=models.CharField(blank=True, choices=[('', ''), ('dz', 'الجزائر'), ('tn', 'تونس'), ('eg', 'مصر'), ('sd', 'السودان'), ('iq', 'العراق'), ('ma', 'المغرب'), ('sa', 'السعودية'), ('ye', 'اليمن'), ('sy', 'سوريا'), ('so', 'الصومال'), ('jo', 'الأردن'), ('ae', 'الإمارات'), ('ly', 'ليبيا'), ('lb', 'لبنان'), ('ps', 'فلسطين'), ('om', 'عمان'), ('kw', 'الكويت'), ('mr', 'موريطانيا'), ('qa', 'قطر'), ('bh', 'البحرين'), ('dj', 'جيبوتي'), ('km', 'جزر القمر'), ('er', 'إريتيريا'), ('eh', 'الصحراء الغربية')], max_length=50),
        ),
        migrations.AddField(
            model_name='project',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projects', to='profiles.Profile'),
        ),
    ]
