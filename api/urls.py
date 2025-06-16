from django.urls import path
from .views import validate_password

urlpatterns = [
    path('validate-password/', validate_password, name='validate-password'),
]