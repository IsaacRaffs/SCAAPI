from django import forms
from .models import Animal, Adotante


class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = ['especie', 'nome', 'sexo', 'esterilizacao', 'nascimento', 'raca', 'pelagem', 'status']
        widgets = {
            'especie': forms.Select(attrs={'class': 'form-select'}),
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome do animal'}),
            'sexo': forms.Select(attrs={'class': 'form-select'}),
            'esterilizacao': forms.Select(attrs={'class': 'form-select'}),
            'nascimento': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'raca': forms.Select(attrs={'class': 'form-select'}),
            'pelagem': forms.Select(attrs={'class': 'form-select'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
        }


class AdotanteForm(forms.ModelForm):
    class Meta:
        model = Adotante
        fields = ['nome', 'email', 'telefone', 'endereco']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome completo'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'email@example.com'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '(11) 99999-9999'}),
            'endereco': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
