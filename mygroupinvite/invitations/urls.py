from django.urls import path
from .views import invite_member, success

urlpatterns = [
    path('', invite_member, name='invite_member'),
    path('success/', success, name='success'),
]
