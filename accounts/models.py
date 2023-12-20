from django.db import models
from django.contrib.auth.models import User

from base.models import School, Course, Year, Unit

class S_register(models.Model):
    student = models.OneToOneField(User, on_delete=models.CASCADE)
    school = models.ForeignKey(School, on_delete=models.DO_NOTHING, null=True)
    course = models.ForeignKey(Course, on_delete=models.DO_NOTHING, null=True, related_name='studentincourse')
    year = models.ForeignKey(Year, on_delete=models.DO_NOTHING, null=True)
    unit = models.ForeignKey(Unit, on_delete=models.DO_NOTHING, null=True)
    image = models.ImageField(upload_to='users/%y/%m/%d', blank=True)
    registration_number = models.CharField(max_length=200, unique=True, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.student
    
class L_register(models.Model):
    lecturer = models.OneToOneField(User, on_delete=models.CASCADE)
    school = models.ForeignKey(School, on_delete=models.DO_NOTHING, null=True)
    course = models.ForeignKey(Course, on_delete=models.DO_NOTHING, null=True, related_name='lecturerassigned')
    year = models.ForeignKey(Year, on_delete=models.DO_NOTHING, null=True)
    unit = models.ForeignKey(Unit, on_delete=models.DO_NOTHING, null=True)
    image = models.ImageField(upload_to='users/%y/%m/%d', blank=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.student
