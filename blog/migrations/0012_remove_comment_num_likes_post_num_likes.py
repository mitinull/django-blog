# Generated by Django 4.2.5 on 2023-09-30 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0011_comment_num_likes"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="comment",
            name="num_likes",
        ),
        migrations.AddField(
            model_name="post",
            name="num_likes",
            field=models.IntegerField(default=0),
        ),
    ]
