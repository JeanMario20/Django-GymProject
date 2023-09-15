from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Miembros
from .forms import MiembrosForm
#from .task import check, imprimir_nombre_miembro
# Create your views here.



def view_table(request):
    dataTable = Miembros.objects.all()
    #imprimir_nombre_miembro.apply_async(countdown=1, repeat=True)
    #task1 = actualizar_dato_periodicamente.appy_async()
    #actualizar_dato_periodicamente.apply_async(countdown=20)
    return render(request, 'table.html', {'dataTable':dataTable})

def addMiembro(request):
    form = MiembrosForm()
    if request.method == 'POST':
        form = MiembrosForm(request.POST)
        if form.is_valid():
            #actualizar_dato_periodicamente.apply_async(countdown=10, repeat=True)
            #imprimir_nombre_miembro.apply_async(countdown=10, repeat=True)
            form.save()
            return render(request, 'add_costumer.html', {'success':True})
    context = {'form':form}
    return render(request, 'add_costumer.html',context)
