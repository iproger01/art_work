# Generated by Django 3.2.8 on 2022-01-23 18:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mailinglist', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contact',
            options={'verbose_name': 'Адрес email', 'verbose_name_plural': 'Адреса email подписчиков'},
        ),
    ]