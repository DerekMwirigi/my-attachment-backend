from django.conf.urls import url
from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views

from .views import (
    SignUp_API,
    StudentLogBook_API,
    StudentLogBookItem_API,
)
urlpatterns = [
    path('sign-in/', jwt_views.TokenObtainPairView.as_view(), name='sign-in'),
    path('sign-up/', SignUp_API.as_view(), name='sign-up'),
    path('student-logbook/', StudentLogBook_API.as_view(), name='student-logbook'),
    path('student-logbook-item/', StudentLogBookItem_API.as_view(), name='student-logbook'),
]
