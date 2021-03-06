# Generated by Django 3.2.2 on 2021-05-19 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_alter_menu_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='coursemessage',
            options={'verbose_name_plural': '课程信息'},
        ),
        migrations.AlterModelOptions(
            name='home',
            options={'verbose_name_plural': ''},
        ),
        migrations.AlterModelOptions(
            name='homeimages',
            options={'verbose_name_plural': '首页图片'},
        ),
        migrations.AlterModelOptions(
            name='referencebooks',
            options={'verbose_name_plural': '参考书'},
        ),
        migrations.AlterModelOptions(
            name='teachingresources',
            options={'verbose_name_plural': '教学资源'},
        ),
        migrations.AddField(
            model_name='coursemessage',
            name='name',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='homeimages',
            name='name',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]
