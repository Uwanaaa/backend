# Generated by Django 5.0 on 2024-03-03 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_usermodel_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='first_name',
            field=models.CharField(verbose_name='First Name'),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='last_name',
            field=models.CharField(verbose_name='Last name'),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='mobile_number',
            field=models.CharField(verbose_name='Phone number'),
        ),
    ]