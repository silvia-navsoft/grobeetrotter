# Generated by Django 3.2 on 2021-04-28 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapplication', '0004_auto_20210428_0616'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_phone',
            field=models.CharField(max_length=20, null=True),
        ),
    ]