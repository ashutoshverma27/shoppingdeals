# Generated by Django 2.1.3 on 2019-08-01 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='url',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
