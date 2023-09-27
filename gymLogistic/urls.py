from django.urls import path
from . import views

urlpatterns = [
    path('table/', views.view_table, name='table'),
    path('add-miembro', views.addMiembro, name="add-mie"),
    path('editMember_or_deleteMember/<str:pk>?', views.editMember_or_deleteMember, name="editMember_or_deleteMember"),
]