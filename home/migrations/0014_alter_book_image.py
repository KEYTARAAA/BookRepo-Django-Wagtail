# Generated by Django 5.0.1 on 2024-01-31 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_book_image_alter_book_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]