# Generated by Django 3.0.7 on 2020-06-21 13:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant_app', '0003_auto_20200621_1912'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Restaurant',
            new_name='RestaurantLocation',
        ),
    ]
