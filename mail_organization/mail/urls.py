from django.urls import path
from . import views

urlpatterns = [
    path('send/', views.send_mail, name='send_mail'),
    path('list/', views.mail_list, name='mail_list'),
]