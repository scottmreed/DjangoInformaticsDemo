from django.db import models

# Create your models here.

class Chemical(models.Model):
    name = models.CharField(max_length=200)
    BP_C = models.CharField(max_length=200, default=0)
    BP_K = models.CharField(max_length=200, default=0)
    smiles = models.CharField(max_length=200, default=0)
    MW = models.CharField(max_length=200, default=0)
