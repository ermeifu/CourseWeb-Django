# Generated by Django 3.2.2 on 2021-05-19 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_auto_20210519_1028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='enabled',
            field=models.BooleanField(default=True),
        ),
    ]
