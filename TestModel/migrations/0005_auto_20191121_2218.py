# Generated by Django 2.2.7 on 2019-11-21 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TestModel', '0004_auto_20191121_2214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activityinfo',
            name='activityPoster',
            field=models.ImageField(upload_to='media'),
        ),
    ]