# Generated by Django 3.2.7 on 2021-11-06 10:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0005_auto_20211106_1010'),
    ]

    operations = [
        migrations.RenameField(
            model_name='seller',
            old_name='pending',
            new_name='applied',
        ),
    ]
