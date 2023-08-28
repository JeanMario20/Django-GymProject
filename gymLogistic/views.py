from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Miembros
# Create your views here.

def reg(request):
    template = loader.get_template('table.html')
    return HttpResponse(template.render())

def view_table(request):
    dataTable = Miembros.objects.all()
    return render(request, 'table.html', {'dataTable':dataTable})
