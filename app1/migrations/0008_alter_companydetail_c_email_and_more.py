# Generated by Django 4.0.5 on 2022-07-08 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0007_companydetail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companydetail',
            name='c_email',
            field=models.EmailField(max_length=200),
        ),
        migrations.AlterField(
            model_name='companydetail',
            name='c_pass',
            field=models.CharField(max_length=200),
        ),
    ]
