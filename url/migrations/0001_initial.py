# Generated by Django 3.2.5 on 2021-08-19 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Url',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(max_length=2048)),
                ('uid', models.CharField(max_length=255)),
            ],
        ),
    ]
