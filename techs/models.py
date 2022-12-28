from django.db import models


class Tech(models.Model):
    name = models.CharField(max_length=50)
    img_url = models.CharField(max_length=200)
