# Generated by Django 3.2.7 on 2021-09-09 12:44

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ChatRoomApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.EmailField(max_length=254, validators=[django.core.validators.RegexValidator(code='invalid_username', message='Username must be Alphanumeric', regex='^[a-z0-9]+[\\._]?[a-z0-9]+[@]\\w+[.]\\w{2,3}$')])),
                ('text', models.TextField(max_length=100, validators=[django.core.validators.RegexValidator(regex='^(?!\\s*$).+')])),
                ('create_date', models.DateField()),
                ('update_date', models.DateField()),
            ],
        ),
        migrations.DeleteModel(
            name='Message',
        ),
    ]