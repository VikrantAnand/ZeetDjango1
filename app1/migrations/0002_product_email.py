# Generated by Django 4.0.5 on 2022-06-29 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='email',
            field=models.EmailField(default='', max_length=254),
        ),
    ]
