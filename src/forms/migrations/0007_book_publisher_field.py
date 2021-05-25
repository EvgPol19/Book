# Generated by Django 3.2.3 on 2021-05-23 00:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0006_auto_20210523_0006'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='publisher_field',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='forms.publisherfield'),
            preserve_default=False,
        ),
    ]