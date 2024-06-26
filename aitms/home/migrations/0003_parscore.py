# Generated by Django 5.0.4 on 2024-04-29 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_vistor_contacts'),
    ]

    operations = [
        migrations.CreateModel(
            name='Parscore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Parscore_student_name', models.CharField(max_length=255)),
                ('Parscore_school_name', models.CharField(max_length=255)),
                ('Parscore_sector', models.CharField(max_length=50)),
                ('Parscore_phone', models.CharField(max_length=10)),
                ('Parscore_email', models.EmailField(max_length=254, unique=True)),
                ('Parscore_location', models.CharField(max_length=60)),
                ('Parscore_career', models.CharField(max_length=80)),
                ('Parscore_career_other', models.CharField(max_length=80)),
            ],
        ),
    ]
