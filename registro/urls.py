from django.urls import path
from . import views

urlpatterns = [
    # ...
    path('api/contactos/', views.ContactoList.as_view(), name='contacto-list'),
    path('api/contactos/<int:pk>/', views.ContactoDetail.as_view(), name='contacto-detail'),
    path('api/contactos-list/', views.contactos_list, name='contactos_list'),
]
