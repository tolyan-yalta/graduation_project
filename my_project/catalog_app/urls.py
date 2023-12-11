from django.urls import path
from . import views

urlpatterns = [
    path('', views.catalog, name='catalog'),
    ]

# http://127.0.0.1:8000/catalog
