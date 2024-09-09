from django.urls import path
from .views import LandmarkListView, LandmarkDetailView

urlpatterns = [
    path('', LandmarkListView.as_view(), name='landmark_list'),
    path('<int:pk>/', LandmarkDetailView.as_view(), name='landmark_detail'),
]
