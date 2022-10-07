# Generated by Django 4.0.5 on 2022-06-27 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=20)),
                ('roll_number', models.IntegerField()),
                ('address', models.CharField(default='', max_length=50)),
            ],
        ),
    ]
