# Generated by Django 4.2.11 on 2024-04-27 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_module', '0004_user_about_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='mobile',
        ),
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.TextField(blank=True, null=True, verbose_name='آدرس'),
        ),
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='temp', verbose_name='تصویر'),
        ),
    ]
