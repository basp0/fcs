# Generated by Django 3.2.7 on 2021-11-06 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0002_auto_20211025_2125'),
    ]

    operations = [
        migrations.AddField(
            model_name='seller',
            name='application_status',
            field=models.BooleanField(default=False),
        ),
    ]