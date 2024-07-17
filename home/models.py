from django.db import models

# Create your models here.

class login(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.email} ({self.password})"

class Student(models.Model):    
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    contact = models.IntegerField()

    def __str__(self):
        return f"{self.name} ({self.email})"
    

