from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mail/', include('mail.urls')),
    path('chat/', include('chat.urls')),
    path('employees/', include('employees.urls')),
]