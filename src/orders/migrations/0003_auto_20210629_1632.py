# Generated by Django 3.2.3 on 2021-06-29 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20210629_1615'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='city',
            field=models.CharField(default='No record', max_length=35, verbose_name='City'),
        ),
        migrations.AddField(
            model_name='order',
            name='country',
            field=models.CharField(default='No record', max_length=35, verbose_name='Country'),
        ),
        migrations.AddField(
            model_name='order',
            name='other',
            field=models.TextField(blank=True, default='No record', max_length=200, null=True, verbose_name='Other information'),
        ),
    ]
