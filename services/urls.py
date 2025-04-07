from services.views import services
from django.urls import path

urlpatterns = [
    path('services/', services, name='services'),
    path('services/<int:id>/', services, name='services'),
]