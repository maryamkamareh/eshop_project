# Generated by Django 4.2.11 on 2024-04-15 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='عنوان')),
                ('email', models.CharField(max_length=300, verbose_name='ایمیل کاربر')),
                ('full_name', models.CharField(max_length=300, verbose_name='نام و نام خوانوادگی')),
                ('message', models.TextField(verbose_name='متن تماس با ما')),
                ('is_read_by_admin', models.BooleanField(verbose_name='خوانده شده توسط ادمین')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')),
                ('response', models.TextField(blank=True, null=True, verbose_name='متن پاسخ تماس با ما')),
            ],
            options={
                'verbose_name': 'تماس با ما',
                'verbose_name_plural': 'لیست تماس با ما',
            },
        ),
    ]
