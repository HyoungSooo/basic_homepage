# Generated by Django 2.1.7 on 2022-11-07 15:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='member_img')),
                ('position', models.CharField(choices=[('PH.D Student', 'PH.D Student'), ('Post Graduate', 'Post Graduate'), ('Undergraduate', 'Undergraduate')], max_length=13)),
                ('image', models.ImageField(upload_to='images/')),
                ('phone', models.CharField(blank=True, max_length=100)),
                ('email', models.EmailField(blank=True, max_length=100)),
                ('address', models.CharField(blank=True, max_length=100)),
                ('join_date', models.DateField(default='2020-01-01')),
            ],
        ),
        migrations.CreateModel(
            name='Name',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('Inter', 'Inter'), ('Res', 'Res'), ('Edu', 'Edu')], max_length=50, verbose_name='')),
                ('des', models.CharField(max_length=500, verbose_name='des')),
                ('start_date', models.DateField(blank=True, null=True, verbose_name='')),
                ('end_date', models.DateField(blank=True, null=True, verbose_name='')),
            ],
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='prof_img')),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=100)),
                ('p_num', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('fax', models.CharField(blank=True, max_length=50, null=True)),
                ('position', models.CharField(max_length=50, verbose_name='position')),
                ('since', models.DateField(verbose_name='date')),
            ],
        ),
        migrations.AddField(
            model_name='name',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prof_time', to='member.Professor'),
        ),
    ]
