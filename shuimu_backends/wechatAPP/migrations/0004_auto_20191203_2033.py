# Generated by Django 2.2.5 on 2019-12-03 12:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wechatAPP', '0003_auto_20191203_2028'),
    ]

    operations = [
        migrations.RenameField(
            model_name='takepartin',
            old_name='userID',
            new_name='openID',
        ),
    ]