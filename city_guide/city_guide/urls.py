from django.contrib import admin
from django.urls import path, include
from cities import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cities/', include('cities.urls')),
    path('landmarks/', include('landmarks.urls')),
    path('', views.index, name='index'),  # Dodaj tę linię
]
