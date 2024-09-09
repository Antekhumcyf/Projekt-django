# cities/views.py
from django.shortcuts import render, get_object_or_404
from .models import City

def city_list(request):
    cities = City.objects.all()
    return render(request, 'cities/city_list.html', {'cities': cities})

def city_detail(request, city_id):
    city = get_object_or_404(City, pk=city_id)
    return render(request, 'cities/city_detail.html', {'city': city})

# cities/views.py
from django.shortcuts import render
from .models import City

def index(request):
    cities = City.objects.all()
    return render(request, 'cities/index.html', {'cities': cities})
