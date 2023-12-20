from django.contrib import admin
from . models import School, Course, Unit, Topic, Year, Marks, Feestatus

admin.site.register([School, Course, Unit, Topic, Year, Marks, Feestatus])