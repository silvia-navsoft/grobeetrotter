# Generated by Django 3.2 on 2021-04-27 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('admin_id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('admin_fname', models.CharField(max_length=30)),
                ('admin_lname', models.CharField(max_length=30)),
                ('admin_email', models.EmailField(max_length=254)),
                ('username', models.CharField(max_length=50)),
                ('admin_password', models.CharField(max_length=50)),
                ('reset_password_times', models.CharField(max_length=30)),
                ('isSuper_admin', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=10)),
                ('isSub_admin', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=10)),
                ('admin_status', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=10)),
            ],
        ),
    ]
