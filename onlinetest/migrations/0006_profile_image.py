# Generated by Django 2.2.10 on 2021-02-04 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinetest', '0005_remove_config_results_list_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]