

from django.urls import path
from .views import contact_get


urlpatterns = [

    path('contact/',contact_get, name='contact'),
]
