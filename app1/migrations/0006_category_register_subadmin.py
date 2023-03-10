# Generated by Django 4.0.5 on 2022-07-03 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_pro'),
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('contact', models.PositiveIntegerField()),
                ('password', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='subadmin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=150)),
                ('contact', models.IntegerField(default=0)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
    ]
