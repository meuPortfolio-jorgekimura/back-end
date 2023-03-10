# Generated by Django 4.1.4 on 2022-12-28 13:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("techs", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Link",
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
                ("git_hub", models.CharField(max_length=200, unique=True)),
                ("vercel", models.CharField(max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="Project",
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
                ("objective", models.TextField()),
                ("img_url", models.CharField(max_length=200, unique=True)),
                ("title", models.CharField(max_length=100)),
                (
                    "link",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="project",
                        to="projects.link",
                    ),
                ),
                (
                    "techs",
                    models.ManyToManyField(related_name="projects", to="techs.tech"),
                ),
            ],
        ),
    ]
