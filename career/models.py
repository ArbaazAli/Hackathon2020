from django.db import models

# Create your models here.
class Choice(models.Model):
    selections = models.CharField(max_length=2000)

    