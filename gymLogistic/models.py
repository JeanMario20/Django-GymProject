from django.db import models

# Create your models here.
tier_list = (
    ("visitante","visitante"),
    ("miebro","miembro"),
    ("VIP","VIP"),
)
class Miembros(models.Model):
    nombreCompleto = models.CharField(max_length=200)
    Tierlist = models.CharField(
        max_length= 20,
        choices= tier_list,
        default="",
    )
    Fecha = models.DateField(auto_now_add=True)
    monto = models.IntegerField()
