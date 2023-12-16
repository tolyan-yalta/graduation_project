# from django.conf.urls import url
# from django.conf.urls import url
from django.urls import path, re_path
from . import views

from django.conf.urls.static import static
from django.conf import settings

app_name = "basket"

urlpatterns = [
    # path('', views.basket_detail, name='basket_detail'),
    # path('add/<int:product_id>', views.basket_add, name='basket_add'),
    # path('remove/<int:product_id>', views.basket_remove, name='basket_remove'),
    re_path(r'^$', views.basket_detail, name='basket_detail'),
    re_path(r'^add/(?P<product_id>\d+)/?$', views.basket_add, name='basket_add'),
    re_path(r'^remove/(?P<product_id>\d+)/?$', views.basket_remove, name='basket_remove'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
