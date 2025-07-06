from core import views  
from django.urls import path, include
from django.contrib import admin
urlpatterns = [
    path('', views.inicio, name='inicio'),  
    path('admin/', admin.site.urls),
    path('auth/', include('core.urls')),
]
