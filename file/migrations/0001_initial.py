# Generated by Django 2.1.7 on 2022-11-06 16:27

from django.db import migrations, models
import django.db.models.deletion
import file.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FileActivity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=200)),
                ('file', models.FileField(upload_to=file.models.make_filename)),
                ('post', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='post.PostActivity')),
            ],
        ),
        migrations.CreateModel(
            name='FileFree',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=200)),
                ('file', models.FileField(upload_to=file.models.make_filename)),
                ('post', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='post.PostFree')),
            ],
        ),
        migrations.CreateModel(
            name='FileJokbo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=200)),
                ('file', models.FileField(upload_to=file.models.make_filename)),
                ('post', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='post.PostJokbo')),
            ],
        ),
        migrations.CreateModel(
            name='FileNotice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=200)),
                ('file', models.FileField(upload_to=file.models.make_filename)),
                ('post', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='post.PostNotice')),
            ],
        ),
        migrations.CreateModel(
            name='FileShare',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=200)),
                ('file', models.FileField(upload_to=file.models.make_filename)),
                ('post', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='post.PostShare')),
            ],
        ),
        migrations.CreateModel(
            name='FileStudy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=200)),
                ('file', models.FileField(upload_to=file.models.make_filename)),
                ('post', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='post.PostStudy')),
            ],
        ),
    ]
