from django.urls import path
from .views import ContactoListCreateView

urlpatterns = [
    path('contactos/', ContactoListCreateView.as_view(), name='contacto-list-create'),
]
