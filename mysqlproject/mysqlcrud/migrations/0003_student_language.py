# Generated by Django 4.0.5 on 2022-06-29 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysqlcrud', '0002_student_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='language',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
    ]
