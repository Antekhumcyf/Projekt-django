# cities/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('', views.city_list, name='city_list'),
    path('city/<int:city_id>/', views.city_detail, name='city_detail'),
]
