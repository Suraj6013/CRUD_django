from django.db import models

# Create your models here.

class login(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    user = User.objects.create_user(username='your_username', password='your_password')
    user.save()

    # login = Login(user=user)
    # login.save()

    def __str__(self):
        return f"{self.username} ({self.password})"

class Student(models.Model):    
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    contact = models.IntegerField()

    def __str__(self):
        return f"{self.name} ({self.email})"
    

