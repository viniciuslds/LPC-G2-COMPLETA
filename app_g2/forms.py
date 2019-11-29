from django import forms

class NOMEForm(forms.Form):
    texto = forms.CharField(max_length=200, widget=forms.Textarea(attrs={'cols': 70, 'rows': 10}))

    def clean(self):
        dados = super().clean()
        texto = dados.get('texto',None)

        return dados
