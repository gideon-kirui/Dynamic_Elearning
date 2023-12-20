from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login_a/', views.user_login, name='login'),
    path('login/', views.login_user, name='loginuser'),
    path('logout/', views.userlogout, name='logout'),
    path('register/', views.user_registration, name='register'),
    path('update_details/', views.UpdateDetails, name='updated_d'),
    path('update_detailsl/', views.LUpdateDetails, name='updated_l'),
    path('addtopic/<int:unit_id>/', views.addtopic, name='addtopic'),
    path('addcat/<int:unit_id>/', views.addtopic, name='addcat'),
    path('edittopic/<int:topic_id>', views.edittopic, name='editt'),
    path('deletetopic/<int:topic_id>', views.deletetopic, name='deletet'),
    path('addmarks/<int:unit_id>', views.addstudentmarks, name='addmarks'),
    path('editmarks/<int:marks_id>', views.editmarks, name='editmarks'),
]