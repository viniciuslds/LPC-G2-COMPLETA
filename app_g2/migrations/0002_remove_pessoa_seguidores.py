# Generated by Django 2.2.7 on 2019-11-28 20:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_g2', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pessoa',
            name='seguidores',
        ),
    ]
