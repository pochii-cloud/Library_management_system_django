# Generated by Django 3.2.3 on 2021-07-22 16:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0020_alter_book_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='date2',
            field=models.DateField(auto_created=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
