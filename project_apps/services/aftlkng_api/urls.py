from django.urls import path, include
from django.conf.urls import url
from .views import ExpressSMS

urlpatterns = [
    url('express-sms/', ExpressSMS.as_view() , name='express_sms')
]