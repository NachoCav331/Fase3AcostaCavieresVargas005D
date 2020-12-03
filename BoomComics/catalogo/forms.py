from django import forms
from .models import Comic


class ComicsForms(forms.ModelForm):
    class Meta:
        model= Comic
        fields = ('id','titulo','autor','resumen','isbn','tipo','formato','precio','imagen')

        widgets = {
             
                'id': forms.TextInput(attrs={'class': 'form-control'}),
                'titulo':forms.TextInput(attrs={'class': 'form-control'}),
                'autor':forms.Select(attrs={'class': 'custom-select mr-sm-2'}),
                'resumen':forms.Textarea(attrs={'class': 'form-control'}),
                'isbn':forms.TextInput(attrs={'class': 'form-control'}),
                'tipo':forms.Select(attrs={'class': 'form-control'}),
                'formato':forms.Select(attrs={'class': 'form-control'}),
                'precio':forms.TextInput(attrs={'class': 'form-control'}),
                'imagen':forms.FileInput(attrs={'class': 'form-control-file'}),
        }
