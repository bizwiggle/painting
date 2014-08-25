from django import forms

from pages.models import Why_Us

class Why_UsForm(forms.ModelForm):
    class Meta:
        model = Why_Us
