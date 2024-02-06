from django.urls import path
from app import views

urlpatterns = [
    path('image/create/', views.image_create, name='image_create'),
]