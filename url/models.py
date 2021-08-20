from django.db import models


class Url(models.Model):
    link = models.CharField(max_length=2048)
    uid = models.CharField(max_length=255)
