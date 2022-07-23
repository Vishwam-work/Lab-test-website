from django.db import models

# Create your models here.
class Admin_signup(models.Model):
    username=models.CharField(max_length=255)
    firstname=models.CharField(max_length=255)
    lastname=models.CharField(max_length=255)
    email=models.EmailField()
    password=models.CharField(max_length=255)
    class Meta:
        db_table='admin'

