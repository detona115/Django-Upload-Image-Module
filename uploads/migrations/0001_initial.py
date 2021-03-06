# Generated by Django 3.0.8 on 2020-07-17 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UploadedFiles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=150)),
                ('dimensao', models.CharField(max_length=30)),
                ('formato', models.CharField(max_length=10)),
                ('arquivo', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='UploadedFilesThumb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=150)),
                ('dimensao', models.CharField(max_length=30)),
                ('formato', models.CharField(max_length=10)),
                ('arquivo', models.ImageField(upload_to='images/')),
                ('thumb', models.ImageField(upload_to='images/thumbnails/')),
            ],
        ),
    ]
