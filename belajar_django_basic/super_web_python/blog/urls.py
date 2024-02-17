# blog/urls.py
from django.urls import path
from .views import blog_view

urlpatterns = [
    path('', base_view, name='blog'),
]