# Generated by Django 3.2.3 on 2021-06-16 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0009_alter_authorfield_author_descrption'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seriesfield',
            name='series',
            field=models.CharField(max_length=50, verbose_name='Books series'),
        ),
    ]
