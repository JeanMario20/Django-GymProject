from django.urls import path
from . import views

urlpatterns = [
    path('table/', views.view_table, name='table'),
]