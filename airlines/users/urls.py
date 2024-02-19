from django.urls import path,include
from .views import user, login_view, refresh_token_view
from rest_framework.routers import DefaultRouter


urlpatterns = [
    path('user', user, name='user'),
    path('login', login_view, name='login'),
    path('refresh', refresh_token_view, name='refresh')
]