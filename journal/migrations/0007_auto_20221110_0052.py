# Generated by Django 2.1.7 on 2022-11-10 00:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0006_auto_20221110_0026'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordering', models.IntegerField(blank=True, null=True)),
                ('title', models.CharField(max_length=500)),
                ('year', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Ypaper', to='journal.Year')),
            ],
        ),
        migrations.AlterField(
            model_name='papers',
            name='year',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Ypatent', to='journal.Year'),
        ),
    ]
