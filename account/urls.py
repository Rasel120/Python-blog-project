from django.urls import path
from .import views



urlpatterns = [
    path('', views.authlogin, name='login'),
    path('logout/', views.authlogout, name='logsout'),
    path('register/', views.authregister, name='registration'),
    path('forgot/', views.authforgot, name='forgotpass'),
    path('profile/', views.authprofile, name='userprofile'),
]
