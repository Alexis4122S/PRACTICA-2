# app_notifications/urls.py
from django.urls import path
from . import views
# app_notifications/urls.py
app_name = 'app_notifications'
urlpatterns = [
    path('index/', views.home, name='index'),
    path('asignar/', views.notifications1, name='lista_Notificaciones'),
]
