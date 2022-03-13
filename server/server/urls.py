# backend/server/server/urls.py file
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.endpoints.urls'))
]

