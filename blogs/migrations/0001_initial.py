# Generated by Django 2.1.3 on 2019-07-31 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('postid', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(max_length=255)),
                ('post', models.TextField()),
                ('date', models.DateTimeField()),
                ('image', models.TextField()),
            ],
        ),
    ]
