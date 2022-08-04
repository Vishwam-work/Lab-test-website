
from django.db import models

# Create your models here.
# class Sampletest(models.Model):
#     samplename=models.CharField(max_length=255)
#     sampledate=models.DateField()
#     samplelocation=models.CharField(max_length=255)
#     class Meta:
#         db_table='Sampletest'
class Sample(models.Model):
    samplename=models.CharField(max_length=255)
    sampledate=models.DateField()
    samplelocation=models.CharField(max_length=255)
    class Meta:
       db_table = 'sample'
