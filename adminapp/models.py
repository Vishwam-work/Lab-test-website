from django.db import models
from django.forms import CharField



# Create your models here.
class Admin_signup(models.Model):
    username=models.CharField(max_length=255)
    firstname=models.CharField(max_length=255)
    lastname=models.CharField(max_length=255)
    email=models.EmailField()
    password=models.CharField(max_length=255)
    class Meta:
        db_table='admin'

class SampleTest(models.Model):
    disin = (
    ('yes','YES'),
    ('no','NO'),
    )
    sample_name=models.CharField(max_length=255)
    sample_location=models.CharField(max_length=255)
    sample_dis=models.CharField(max_length=255)
    # sample matrix
    sample_matrix=models.CharField(max_length=255)
    # sample system
    sample_system=models.CharField(max_length=255)
    # sample sampling
    sample_sampling=models.CharField(max_length=255)
    gridRadios=models.CharField(max_length=255,choices=disin)
    test1=models.CharField(max_length=255)
    test2=models.CharField(max_length=255)
  
    class Meta:
       db_table = 'analysis'
