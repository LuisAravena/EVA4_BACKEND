from rest_framework.viewsets import ModelViewSet
from django.shortcuts import render, redirect, get_object_or_404
from .models import Numero, Reporte, Usuario
from .serializers import NumeroSerializer, ReporteSerializer, UsuarioSerializer
import csv
from django.http import HttpResponse
from .forms import NumeroForm  # Asegúrate de tener este formulario creado en forms.py


# ---------------------------
# API REST: ModelViewSets
# ---------------------------

class NumeroViewSet(ModelViewSet):
    """API para el modelo Numero."""
    queryset = Numero.objects.all()
    serializer_class = NumeroSerializer


class ReporteViewSet(ModelViewSet):
    """API para el modelo Reporte."""
    queryset = Reporte.objects.all()
    serializer_class = ReporteSerializer


class UsuarioViewSet(ModelViewSet):
    """API para el modelo Usuario."""
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


# ---------------------------
# Funcionalidad de exportar a CSV
# ---------------------------
def exportar_csv(request):
    """Vista para exportar números a CSV."""
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="numeros.csv"'

    writer = csv.writer(response)
    writer.writerow(['Número', 'Es Spam', 'Reportes'])  # Escribir encabezados en el CSV

    # Escribir los datos
    for numero in Numero.objects.all():
        writer.writerow([numero.numero, numero.es_spam, numero.reportes])

    return response


# ---------------------------
# Vistas para los Templates
# ---------------------------

def numero_list(request):
    """Lista todos los números registrados en la base de datos."""
    numeros = Numero.objects.all()
    return render(request, 'numero_list.html', {'numeros': numeros})


def numero_create(request):
    """Crea un nuevo número."""
    if request.method == 'POST':
        form = NumeroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('numero_list')
    else:
        form = NumeroForm()
    return render(request, 'numero_form.html', {'form': form, 'numero': None})


def numero_update(request, pk):
    """Actualiza un número existente."""
    numero = get_object_or_404(Numero, pk=pk)
    if request.method == 'POST':
        form = NumeroForm(request.POST, instance=numero)
        if form.is_valid():
            form.save()
            return redirect('numero_list')
    else:
        form = NumeroForm(instance=numero)
    return render(request, 'numero_form.html', {'form': form, 'numero': numero})


def numero_delete(request, pk):
    """Elimina un número después de confirmación."""
    numero = get_object_or_404(Numero, pk=pk)
    if request.method == 'POST':
        numero.delete()
        return redirect('numero_list')
    return render(request, 'numero_confirm_delete.html', {'numero': numero})
