# Generated by Django 3.0.4 on 2020-04-06 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0002_auto_20200406_0528'),
    ]

    operations = [
        migrations.AlterField(
            model_name='input',
            name='input_file',
            field=models.ImageField(upload_to='media/input1/'),
        ),
    ]
