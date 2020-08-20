from django.db import models

class CV(models.Model):

    name = models.CharField(max_length= 42)