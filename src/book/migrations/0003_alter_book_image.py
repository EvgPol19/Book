# Generated by Django 3.2.3 on 2021-06-09 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_remove_book_number_of_pages'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(upload_to='book/%Y/%m/%d/', verbose_name='Book image'),
        ),
    ]
