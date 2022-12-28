from django.db import models


class Project(models.Model):
    objective = models.TextField()
    img_url = models.CharField(max_length=200, unique=True)
    title = models.CharField(max_length=100)

    links = models.OneToOneField(
        "projects.Link",
        on_delete=models.CASCADE,
        related_name="project",
    )

    techs = models.ManyToManyField("techs.Tech", related_name="projects")


class Link(models.Model):
    git_hub = models.CharField(max_length=200, unique=True)
    vercel = models.CharField(max_length=200, unique=True)
