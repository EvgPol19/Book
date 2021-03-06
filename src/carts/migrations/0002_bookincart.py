# Generated by Django 3.2.3 on 2021-06-22 07:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_alter_book_image'),
        ('carts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookInCart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1, verbose_name='Quantity')),
                ('unit_price', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Unit price')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='book.book', verbose_name='Book')),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carts.cart', verbose_name='Cart')),
            ],
        ),
    ]
