# Generated by Django 2.1.7 on 2022-11-10 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0011_auto_20221109_1524'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='position',
            field=models.CharField(choices=[('PH.D', 'PH.D'), ('Post_Graduate', 'Post_Graduate'), ('Undergraduate', 'Undergraduate')], max_length=13),
        ),
    ]