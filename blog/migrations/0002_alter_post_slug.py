# Generated by Django 4.2.5 on 2023-09-22 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="slug",
            field=models.SlugField(primary_key=True, serialize=False, unique=True),
        ),
    ]