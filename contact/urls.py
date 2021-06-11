from django.urls import path
from .import views


urlpatterns = [
    path('', views.index, name='home'),
    path('contact/', views.contact_view, name='contact'),
    path('services/', views.services, name='services'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('search/', views.search, name='search'),
]
