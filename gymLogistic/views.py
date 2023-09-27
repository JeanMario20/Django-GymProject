from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Miembros
from .forms import MiembrosForm
#from .task import check, imprimir_nombre_miembro
# Create your views here.



def view_table(request):
    busqueda = request.GET.get('busqueda','')
    if busqueda:
        dataTable = Miembros.objects.filter(nombreCompleto__contains=busqueda)
    else:
        dataTable = Miembros.objects.all()
    return render(request, 'table.html' , {'dataTable':dataTable})
    

def addMiembro(request):
    form = MiembrosForm()
    if request.method == 'POST':
        form = MiembrosForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'add_costumer.html', {'success':True})
    context = {'form':form}
    return render(request, 'add_costumer.html',context)

def editMember_or_deleteMember (request , pk):
    member_id = Miembros.objects.get(id=pk)
    form = MiembrosForm(instance=member_id)

    if request.method == "POST":
        form = MiembrosForm(request.POST, instance=member_id)
        if form.is_valid():
            if 'update' in request.POST:
                form.save()
                return redirect('../table/')
            elif 'delete' in request.POST:
                member_id.delete()
                return redirect('../table/')
    context = {'form':form, 'member_id':member_id}
    return render(request, 'update_costumer.html', context)

def delete_Member(request, pk):
    member_data = Miembros.objects.get(id=pk)
    if request.method == 'POST':
        member_data.delete()
    context = {'member_data': member_data}
    return render(request, '../delete', context)
