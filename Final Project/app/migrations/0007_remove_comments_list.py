# Generated by Django 2.0.7 on 2018-08-06 23:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_comments'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='list',
        ),
    ]
