# Generated by Django 2.1.3 on 2019-08-02 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_posts'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='url',
            new_name='amazon_url',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='price',
            new_name='price_on_amazon',
        ),
        migrations.AddField(
            model_name='product',
            name='flipkart_url',
            field=models.CharField(default=-1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='price_on_flipkart',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
