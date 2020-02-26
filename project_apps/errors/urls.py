from django.conf.urls import url
from django.urls import path, include
from . import views

urlpatterns = [
    path('/', views.error, name='error-generic'),
    path('/generic/', views.generic_error, name='error-generic'),
]