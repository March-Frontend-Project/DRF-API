# Generated by Django 4.1.10 on 2023-07-13 14:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jazzyburger', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='categories',
        ),
    ]
