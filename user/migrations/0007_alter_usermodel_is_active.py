# Generated by Django 5.0.2 on 2024-03-06 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_alter_usermodel_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='is_active',
            field=models.BooleanField(),
        ),
    ]
