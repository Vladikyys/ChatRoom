# Generated by Django 3.2.7 on 2021-09-09 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.EmailField(max_length=254)),
                ('text', models.TextField()),
                ('create_date', models.DateField()),
                ('update_date', models.DateField()),
            ],
        ),
    ]
