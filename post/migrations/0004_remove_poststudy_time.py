# Generated by Django 2.1.7 on 2022-11-10 01:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_auto_20221110_0127'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='poststudy',
            name='time',
        ),
    ]