from django import forms
from .models import Main

# class EmailForm(forms.Form):
#     email = forms.EmailField()


class EmailForm(forms.ModelForm):
    class Meta:
        model = Main
        fields = ["email"]
