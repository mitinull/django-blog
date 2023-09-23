# Generated by Django 4.2.5 on 2023-09-23 07:28

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0002_alter_post_slug"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="date",
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name="post",
            name="content",
            field=models.TextField(
                validators=[django.core.validators.MinLengthValidator(10)]
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="photographer",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="posts",
                to="blog.photographer",
            ),
        ),
    ]
