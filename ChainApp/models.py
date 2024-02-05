from django.db import models

# Create your models here.

class ChainModel(models.Model):
    name = models.CharField(max_length = 100)
    email = models.EmailField()
    
class DataTable(models.Model):
    name = models.CharField(max_length = 100)
    email = models.EmailField()