# Generated by Django 3.2.2 on 2021-05-18 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_alter_teachingresources_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReferenceBooks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('img', models.URLField()),
            ],
        ),
    ]
