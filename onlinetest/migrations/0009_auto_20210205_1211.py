# Generated by Django 2.2.10 on 2021-02-05 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinetest', '0008_auto_20210205_0054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='config',
            name='result_release_time',
            field=models.BooleanField(default=False, help_text='To make results visible or not'),
        ),
    ]