from django.contrib import admin
from django.urls import path, include, re_path
# from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('index_app.urls')),
    # path('basket/', include('basket_app.urls', namespace='basket')),
    re_path(r'^basket/', include('basket_app.urls', namespace='basket')),
    # path('catalog/', include('catalog_app.urls', namespace='catalog')),
    path('catalog/', include('catalog_app.urls')),
    path('about/', include('about_app.urls')),
    path('users/', include('users_app.urls', namespace="users")),
    re_path(r'^orders/', include('orders_app.urls', namespace='orders')),
    # re_path(r'^orders/', include('orders_app.urls')),
    # path('orders/', include('orders_app.urls', namespace='orders')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
