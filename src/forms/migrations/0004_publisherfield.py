# Generated by Django 3.2.3 on 2021-05-23 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0003_genrefield'),
    ]

    operations = [
        migrations.CreateModel(
            name='PublisherField',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publisher', models.CharField(max_length=30, verbose_name='Books publisher')),
            ],
        ),
    ]
