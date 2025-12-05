from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    usertype=models.CharField(max_length=50)
    address=models.CharField(max_length=255,null=True)
    phone_number=models.IntegerField(null=True)

class Teacher(models.Model):
    teacher_id=models.ForeignKey(User,on_delete=models.CASCADE)
    salary=models.IntegerField()
    experience=models.IntegerField()

class Student(models.Model):
    student_id=models.ForeignKey(User,on_delete=models.CASCADE)
    guardian=models.CharField(max_length=30)

class Trainer(models.Model):
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    email=models.EmailField(max_length=30)
    password=models.CharField(max_length=20)
    age=models.IntegerField()
    class Meta:
        db_table="trainee"

class Bookss(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    summary = models.TextField()
    isbn = models.CharField(max_length=13,unique=True)