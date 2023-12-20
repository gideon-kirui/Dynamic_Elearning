from django.urls import path
from . import views

app_name = 'base'

urlpatterns = [
    path('', views.home, name='home'),
    path('school/<int:sch_id>', views.school, name='school'),
    path('course<int:course_id>', views.course, name='course'),
    path('unit/<int:unit_id>', views.unit, name='unit')
]