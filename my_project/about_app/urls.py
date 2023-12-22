from django.urls import path
# from . import views
from .views import about, contacts

urlpatterns = [
    path('', about, name='about'),
    path('contacts/', contacts, name='contacts'),
    # path('gallery/', gallery, name='gallery'),
    ]

# http://127.0.0.1:8000/about
# http://127.0.0.1:8000/about/contacts
# http://127.0.0.1:8000/about/gallery
