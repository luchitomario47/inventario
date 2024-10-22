from django.shortcuts import render
from .models import InvCab, InvConteo, InvDet

def home(request):
    cabeceras = InvCab.objects.all()
    return render(request, 'gestionInventarios.html', {"Inventarios": cabeceras})  # Asegúrate de que el nombre del archivo sea correcto
