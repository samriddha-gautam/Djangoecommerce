from django.db import models

# Create your models here.

class College(models.Model):
  name = models.CharField(max_length=50)
  location = models.CharField(max_length=50)

class Student(models.Model):
  rollNo= models.IntegerField()
  name = models.CharField(max_length=50)
  address = models.CharField(max_length=50)
  birth_date= models.DateField()
  college= models.ForeignKey(College, on_delete=models.CASCADE)

#   relation-->3 tyes
  #one to one, one to many/ many to one, many to many
  