# Generated by Django 3.2.8 on 2021-10-25 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimage',
            name='image',
            field=models.ImageField(upload_to='media'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='photo_url',
            field=models.ImageField(blank=True, null=True, upload_to='media'),
        ),
    ]
