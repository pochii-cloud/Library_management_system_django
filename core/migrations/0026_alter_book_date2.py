# Generated by Django 3.2.3 on 2021-07-23 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0025_book_total_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='date2',
            field=models.DateField(null=True),
        ),
    ]
