from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Miembros
from .forms import MiembrosForm
from django.utils import timezone
# Create your views here.

def reg(request):
    template = loader.get_template('table.html')
    return HttpResponse(template.render())

def view_table(request):
    dataTable = Miembros.objects.all()
    return render(request, 'table.html', {'dataTable':dataTable})

def addMiembro(request):
    form = MiembrosForm()
    if request.method == 'POST':
        form = MiembrosForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'add_costumer.html', {'success':True})
    context = {'form':form}
    return render(request, 'add_costumer.html',context)
