# Generated by Django 3.2.2 on 2021-05-18 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_coursemessage_introimg'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeachingResources',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('url', models.URLField()),
            ],
        ),
    ]