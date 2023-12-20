from django.urls import path, re_path
from . import views

from django.conf.urls.static import static
from django.conf import settings

app_name = "catalog"

urlpatterns = [
    path('', views.catalog, name='catalog'),
    # path('category/<int:cat_id>/', views.show_category, name='category'),
    path('category/<slug:cat_slug>/', views.show_category, name='category'),
    # path('product/<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
    re_path(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$',
        views.product_detail, name='product_detail'),
    ]

# включаем возможность обработки картинок
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# http://127.0.0.1:8000/catalog

