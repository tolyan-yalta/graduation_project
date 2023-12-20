from django.urls import path, re_path
from . import views
# from orders_app.views import order_create

app_name = "orders"

urlpatterns = [
    re_path(r'^create/$', views.order_create, name='order_create'),
    # path('create/', views.order_create, name='order_create'),
]
