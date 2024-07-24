from django.urls import path
from common.views import home

urlpatterns = [
    path('', home, name='home'),
]
