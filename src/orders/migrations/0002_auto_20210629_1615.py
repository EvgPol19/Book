# Generated by Django 3.2.3 on 2021-06-29 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='contact',
        ),
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.CharField(default='No record', max_length=150, verbose_name='Address'),
        ),
        migrations.AddField(
            model_name='order',
            name='phone',
            field=models.CharField(default='No record', max_length=20, verbose_name='Phone'),
        ),
    ]