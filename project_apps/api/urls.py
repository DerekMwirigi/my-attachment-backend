from django.conf.urls import url
from django.urls import path, include
from .views import (
    SignIn_API,
    SignUp_API,
    StudentLogBook_API,
    LecturerStudentAssingment_APS
)
urlpatterns = [
    path('sign-in/', SignIn_API.as_view(), name='sign-in'),
    path('sign-up/', SignUp_API.as_view(), name='sign-up'),
    path('student-logbook/', StudentLogBook_API.as_view(), name='student-logbook'),
    path('student-logbook-item/', StudentLogBook_API.as_view(), name='student-logbook'),
    path('lecturer-student-assignment/', LecturerStudentAssingment_APS.as_view(), name='lecturer-student-assignment'),
    path('student-attachment-location/', LecturerStudentAssingment_APS.as_view(), name='lecturer-student-assignment'),
]
