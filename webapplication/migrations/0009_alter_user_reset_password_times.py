# Generated by Django 3.2 on 2021-04-30 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapplication', '0008_alter_user_reset_password_times'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='reset_password_times',
            field=models.IntegerField(default=0),
        ),
    ]
