# Generated by Django 2.1.3 on 2019-08-01 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_blogpost_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='postid',
            field=models.AutoField(primary_key=True, serialize=False, unique=True),
        ),
    ]
