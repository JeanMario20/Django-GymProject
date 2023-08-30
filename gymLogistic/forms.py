from django.forms import ModelForm
from .models import Miembros
from django.utils import timezone

class MiembrosForm(ModelForm):
    class Meta:
        model = Miembros
        fields = ['nombreCompleto', 'Tierlist', 'monto']

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.Fecha = timezone.now()
        if commit:
            instance.save()
        return instance