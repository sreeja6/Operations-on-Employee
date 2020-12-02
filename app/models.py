from django.db import models

class Employee(models.Model):
    no = models.AutoField(primary_key=True)
    idno = models.IntegerField(unique=True)
    name = models.CharField(max_length=30)
    salary = models.FloatField()