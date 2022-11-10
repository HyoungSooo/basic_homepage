# Generated by Django 2.1.7 on 2022-11-09 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='address',
        ),
        migrations.AlterField(
            model_name='name',
            name='category',
            field=models.CharField(choices=[('Res', 'Res'), ('Inter', 'Inter'), ('Edu', 'Edu')], max_length=50, verbose_name=''),
        ),
    ]
