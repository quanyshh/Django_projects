from django import forms


class ModelForm(forms.Form):
    file = forms.ImageField()
