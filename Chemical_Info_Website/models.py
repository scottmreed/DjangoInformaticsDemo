from django.db import models

# Create your models here.

class Chemical(models.Model):
    name = models.CharField(max_length=200)
    BP_C = models.FloatField
    BP_K = models.FloatField
    smiles = models.CharField(max_length=200)
    MW = models.FloatField
