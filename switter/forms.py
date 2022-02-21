from django import forms
from .models import Sweet


class SweetForm(forms.ModelForm):
    body = forms.CharField(
        required=True,
        widget=forms.widgets.Textarea(
            attrs={
                "placeholder": "New Sweet...",
                "class": "textarea is-success is-medium",
            }
        ),
        label="",
    )
    draft = forms.CheckboxInput()
    re_sweet = forms.CheckboxInput()

    class Meta:
        model = Sweet
        exclude = ('user', )
