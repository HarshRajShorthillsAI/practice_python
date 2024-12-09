from django.db import models

# Create your models here.

class Student(models.Model):
    # id = models.AutoField() is automatically added by Django
    name = models.CharField(max_length=50)
    age = models.IntegerField(default=18)
    email = models.EmailField(null=True, blank=True)
    address = models.TextField(null=True, blank=True) #modified for creating second migration script
    image = models.ImageField()
    file = models.FileField()
    
class Car(models.Model):
    name = models.CharField(max_length=20)
    speed = models.IntegerField(default=50)

    def __str__(self) -> str:
        return f"Car name: {self.name}, Car speed: {self.speed}\n"