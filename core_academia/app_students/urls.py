
from django.urls import path
from . import views

app_name = 'app_students'  # This is the namespace for the app
urlpatterns = [
    path('estudiantes/', views.home, name='index'),  # List all students
    path('list_students/', views.list_students1, name='list_students1'),  # List all students
    
]
