# Generated by Django 3.2.3 on 2021-06-30 14:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('carts', '0003_alter_bookincart_cart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='carts', to=settings.AUTH_USER_MODEL, verbose_name='Cart'),
        ),
    ]
