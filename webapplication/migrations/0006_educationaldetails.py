# Generated by Django 3.2 on 2021-04-28 11:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapplication', '0005_user_user_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='EducationalDetails',
            fields=[
                ('edu_id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('school_name', models.CharField(max_length=255, null=True)),
                ('college_name', models.CharField(max_length=255, null=True)),
                ('edu_details_status', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=10)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapplication.user')),
            ],
        ),
    ]
