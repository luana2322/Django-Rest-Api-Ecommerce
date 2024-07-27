from django.db import models

# Create your models here.
class User(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  gpa = models.FloatField()
  email = models.EmailField()
  gender=models.CharField(max_length=225)

def __str__(self):
    return self.name
