# Generated by Django 3.2.20 on 2023-08-30 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(auto_created=True, unique=True),
        ),
    ]