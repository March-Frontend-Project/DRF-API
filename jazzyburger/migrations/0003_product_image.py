# Generated by Django 4.1.10 on 2023-07-14 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jazzyburger', '0002_remove_product_categories'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default=' ', upload_to='product_images/'),
        ),
    ]