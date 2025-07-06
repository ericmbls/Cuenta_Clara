from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),           
    path('home/', views.home, name='home'),            
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.registro, name='register'),
    path('password-reset/', views.password_reset, name='password_reset'),
    path('password-reset/done/', views.password_reset_done, name='password_reset_done'),
    path('password-reset/confirm/<uidb64>/<token>/', views.password_reset_confirm, name='password_reset_confirm'),
    path('password-reset/complete/', views.password_reset_complete, name='password_reset_complete'),
path('switcher/', views.auth_switcher, name='auth_switcher'),
]
