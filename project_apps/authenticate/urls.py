from django.conf.urls import url
from django.views.generic import RedirectView
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views as authenticate_views

urlpatterns = [
    path('/', RedirectView.as_view(url='/')),
    path('', auth_views.LoginView.as_view(template_name='auth/sign-in.html'), name='sign-in'),
    path('/sign-up/', authenticate_views.sign_up, name='sign-up'),
    path('/sign-in/', auth_views.LoginView.as_view(template_name='auth/sign-in.html'), name='sign-in'),
    path('/sign-out/', auth_views.LogoutView.as_view(template_name='auth/sign-out.html'), name='sign-out')
]