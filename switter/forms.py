from django import forms
from .models import Sweet


class SweetForm(forms.ModelForm):
    body = forms.CharField(required=True)
    draft = forms.CheckboxInput()
    re_sweet = forms.CheckboxInput()

    class Meta:
        model = Sweet
        exclude = ('user', )
