from django import forms
from django.db.models import Q
from .models import Animal, Adotante


class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = ['especie', 'nome', 'foto', 'sexo', 'esterilizacao', 'nascimento', 'raca', 'pelagem', 'status', 'adotado']
        widgets = {
            'especie': forms.Select(attrs={'class': 'form-select'}),
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome do animal'}),
            'foto': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'sexo': forms.Select(attrs={'class': 'form-select'}),
            'esterilizacao': forms.Select(attrs={'class': 'form-select'}),
            'nascimento': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'raca': forms.Select(attrs={'class': 'form-select'}),
            'pelagem': forms.Select(attrs={'class': 'form-select'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
            'adotado': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

    def clean_foto(self):
        foto = self.cleaned_data.get('foto')
        if not foto:
            return foto
        # Validate file size (<= 3MB)
        max_size = 3 * 1024 * 1024
        if foto.size > max_size:
            raise forms.ValidationError('A imagem deve ter no máximo 3 MB.')
        # Validate content type
        content_type = getattr(foto, 'content_type', '')
        allowed = ['image/jpeg', 'image/png']
        if content_type not in allowed:
            raise forms.ValidationError('Formato inválido. Use JPG ou PNG.')
        return foto


class AdotanteForm(forms.ModelForm):
    animais = forms.ModelMultipleChoiceField(
        queryset=Animal.objects.none(),
        required=False,
        widget=forms.SelectMultiple(attrs={'class': 'form-select', 'size': 8})
    )

    class Meta:
        model = Adotante
        fields = ['nome', 'email', 'telefone', 'endereco', 'animais']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome completo'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'email@example.com'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '(11) 99999-9999'}),
            'endereco': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            self.fields['animais'].queryset = Animal.objects.filter(Q(adotado=False) | Q(adotante=self.instance))
            self.fields['animais'].initial = self.instance.animais.all()
        else:
            self.fields['animais'].queryset = Animal.objects.filter(adotado=False)

    def save(self, commit=True):
        adotante = super().save(commit=commit)
        selected_animais = self.cleaned_data.get('animais')
        if commit and selected_animais is not None:
            Animal.objects.filter(adotante=adotante).exclude(pk__in=[animal.pk for animal in selected_animais]).update(adotante=None, adotado=False)
            for animal in selected_animais:
                animal.adotante = adotante
                animal.adotado = True
                animal.save(update_fields=['adotante', 'adotado'])
        return adotante
