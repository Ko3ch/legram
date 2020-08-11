from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    url(r'login/', auth_views.LoginView.as_view(template_name="registration/login.html"), name = 'login'),
    url(r'logout/', auth_views.LogoutView.as_view(template_name="registration/logout.html"), name = 'logout'),
    url(r'register/', views.register_view, name = 'gram-register'),
]