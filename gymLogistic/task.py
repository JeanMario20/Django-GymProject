from __future__ import absolute_import, unicode_literals
from celery import shared_task, app 
from .models import Miembros
from django.utils import timezone
from datetime import timedelta, datetime
import time 


@shared_task
def add(x,y):
    return x + y

#@shared_task.on_after_configure.connect
#def setup_periodic_tasks(sender, **kwargs):
#    sender.add_periodic_task(10.0, actualizar_dato_periodicamente.s(), name='Actualiza todos los datos cada 10 segundos')
        
@shared_task()
def actualizar_dato_periodicamente():
    ahora = datetime.now().date()
    inicio = ahora - timedelta(days=1)
    objs = Miembros.objects.filter(Fecha__lte=inicio)
    for obj in objs:
        obj.monto += 200
        obj.Fecha = datetime.now().date()
        print(f"el que debe es {obj.nombreCompleto}")
        print(f"su monto aumento a: {obj.monto}")
        print(f"su fecha limite fue el: {inicio}")
        print(f"su nueva fecha limite es el {obj.Fecha}")
        obj.save()
@shared_task
def check():
    objs = Miembros.objects.all()
    for obj in objs:
        obj.nombreCompleto = "esto es una prueba"

@shared_task
def imprimir_nombre_miembro():
    timepo_limite = timezone.now() - timezone.timedelta(seconds=10)
    objs = Miembros.objects.filter(Fecha__gte=timepo_limite)
    for obj in objs:
        obj.monto += 200
        print(f"el monto de {obj.nombreCompleto} fue cambiado a {obj.monto} monto")
        obj.save()