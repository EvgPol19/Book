# Generated by Django 3.2.3 on 2021-06-15 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0008_auto_20210525_1238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authorfield',
            name='author_descrption',
            field=models.TextField(blank=True, null=True, verbose_name='Author description'),
        ),
    ]