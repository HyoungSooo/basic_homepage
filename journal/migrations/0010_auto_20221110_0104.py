# Generated by Django 2.1.7 on 2022-11-10 01:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0009_auto_20221110_0100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patents',
            name='ordering',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
