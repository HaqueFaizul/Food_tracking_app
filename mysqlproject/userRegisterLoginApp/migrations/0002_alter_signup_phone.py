# Generated by Django 4.0.5 on 2022-07-04 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userRegisterLoginApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signup',
            name='phone',
            field=models.IntegerField(max_length=20),
        ),
    ]
