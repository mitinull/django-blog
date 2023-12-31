# Generated by Django 4.2.5 on 2023-09-22 11:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Photographer",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("image", models.CharField(max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Tag",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("caption", models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name="Post",
            fields=[
                ("title", models.CharField(max_length=100)),
                (
                    "slug",
                    models.CharField(max_length=100, primary_key=True, serialize=False),
                ),
                ("image", models.CharField(max_length=500)),
                ("content", models.CharField(max_length=2000)),
                (
                    "photographer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="blog.photographer",
                    ),
                ),
                ("tags", models.ManyToManyField(to="blog.tag")),
            ],
        ),
    ]
