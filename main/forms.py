from django import forms
from . models import verificate_photo_client

class verifyForm(forms.ModelForm):
    class Meta:
        model = verificate_photo_client
        fields = ['photo1']