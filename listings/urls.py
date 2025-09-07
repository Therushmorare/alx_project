from django.urls import path
from . import views

urlpatterns = [
    path('properties/', views.api_overview, name='property-list'),
    # add other API endpoints here
]

