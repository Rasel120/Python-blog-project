from django.urls import path
from .import views


urlpatterns = [
    path('', views.pras, name='praa'),
    # path('search/', views.search, name='search'),

]