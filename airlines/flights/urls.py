from django.urls import path
from .views import rad

urlpatterns = [
    path('',view=rad)
]
