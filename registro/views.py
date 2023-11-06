# En tu archivo views.py

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Contacto
from .serializers import ContactoSerializer
from django.shortcuts import render

class ContactoList(generics.ListCreateAPIView):
    queryset = Contacto.objects.all()
    serializer_class = ContactoSerializer
    #permission_classes = [IsAuthenticated]

class ContactoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contacto.objects.all()
    serializer_class = ContactoSerializer
    #permission_classes = [IsAuthenticated]

def contactos_list(request):
    return render(request, 'agenda/contactos_list.html')
