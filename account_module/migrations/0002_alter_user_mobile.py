# Generated by Django 4.2.11 on 2024-04-20 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_module', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='mobile',
            field=models.CharField(max_length=20, null=True, verbose_name='تلفن همراه'),
        ),
    ]
