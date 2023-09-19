from django.urls import path
from . import views

urlpatterns = [
    path('table/', views.view_table, name='table'),
    path('add-miembro', views.addMiembro, name="add-mie"),
    path('edit-miembro/<str:pk>?', views.editMember, name="edit-miembro"),
]