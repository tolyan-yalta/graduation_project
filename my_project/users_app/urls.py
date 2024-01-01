from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
# from my_project import settings
# from django.contrib.auth import views as auth_views
 
app_name = "users"

urlpatterns = [
    # path('login/', views.login_user, name='login'),
    path('login/', views.LoginUser.as_view(), name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register, name='register'),
    # path('logout/', LogoutView.as_view(next_page=settings.LOGOUT_REDIRECT_URL), name='logout'),
    # path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    # path('logout/', LogoutView.as_view(), name='logout'),
]

# http://127.0.0.1:8000
# http://127.0.0.1:8000/users/login
# http://127.0.0.1:8000/users/logout
