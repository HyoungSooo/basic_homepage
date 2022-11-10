# Generated by Django 2.1.7 on 2022-11-10 01:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0008_auto_20221110_0054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='papers',
            name='year',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Ypaper', to='journal.Year'),
        ),
        migrations.AlterField(
            model_name='patents',
            name='year',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Ypatent', to='journal.Year'),
        ),
    ]
