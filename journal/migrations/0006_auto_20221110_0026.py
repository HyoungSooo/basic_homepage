# Generated by Django 2.1.7 on 2022-11-10 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0005_auto_20221110_0025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conferences',
            name='ordering',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='papers',
            name='ordering',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='projects',
            name='ordering',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]