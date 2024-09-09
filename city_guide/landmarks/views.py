from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Landmark

class LandmarkListView(ListView):
    model = Landmark
    template_name = 'landmarks/landmark_list.html'
    context_object_name = 'landmarks'

class LandmarkDetailView(DetailView):
    model = Landmark
    template_name = 'landmarks/landmark_detail.html'
    context_object_name = 'landmark'
