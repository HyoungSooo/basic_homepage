# Generated by Django 2.1.7 on 2022-11-10 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0012_auto_20221110_1519'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='position',
            field=models.CharField(choices=[('PH_D', 'PH_D'), ('Post_Graduate', 'Post_Graduate'), ('Undergraduate', 'Undergraduate')], max_length=13),
        ),
    ]
