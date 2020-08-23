from django.conf.urls import url
from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views
from django.contrib import admin

from .views import (
    SignUp_API,
    Account_API,
    StudentLogBook_API,
    StudentLogBookItem_API,
    LecturerStudentAssignment_API
)

admin.site.site_header = "Attachment Administration"
admin.site.site_title = "Attachment Administration"
admin.site.index_title = "Attachment Administration"


urlpatterns = [
    path('sign-in/', jwt_views.TokenObtainPairView.as_view(), name='sign-in'),
    path('account/', Account_API.as_view(), name='account'),
    path('sign-up/', SignUp_API.as_view(), name='sign-up'),
    path('student-logbook/', StudentLogBook_API.as_view(), name='student-logbook'),
    path('student-logbook-item/', StudentLogBookItem_API.as_view(), name='student-logbook'),
    path('lecturer-student-assignments/', LecturerStudentAssignment_API.as_view(), name='lecturer-student-assignments'),
]
