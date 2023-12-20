from django.db import models
from django.contrib.auth.models import User

class School(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name
    
class Course(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='course')
    title = models.CharField(max_length=200, unique=True)
    def __str__(self):
        return self.title

class Year(models.Model):
    name = models.CharField(max_length=100, unique=True)
    course =models.ManyToManyField(Course)
    def __str__(self):
        return self.name

class Unit(models.Model):
    year = models.ForeignKey(Year, on_delete=models.CASCADE, related_name='unit')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='courseunit')
    lecturer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='unittakenby', null=True, blank=True)
    title = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    register = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title

class Topic(models.Model):
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, related_name='topic')
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    file = models.FileField(upload_to='files/', blank=True, null=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class Marks(models.Model):
    student = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True, related_name='stdmarks')
    unit = models.OneToOneField(Unit, on_delete=models.CASCADE, related_name='unitmarks',null=True, blank=True)
    lecturer = models.ForeignKey(User, related_name='marksbylec', on_delete=models.DO_NOTHING, null=True, blank=True)
    grade = models.CharField(max_length=1)
    percentage = models.IntegerField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.grade
    
class Feestatus(models.Model):
    student = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    status = models.BooleanField(default=False)
    paid = models.BigIntegerField()
    pedding = models.BigIntegerField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.student}, Ksh.{self.pedding} arreas'
