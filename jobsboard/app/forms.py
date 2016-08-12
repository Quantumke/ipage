from django import forms
from .models import contactus, prospects

class ContactDetails(forms.ModelForm):

    class Meta:
        model=contactus
        fields=('name', 'email', 'phone', 'message',)

class ProspectusForm(forms.ModelForm):

    class Meta:
        model= prospects
        fields=('name', 'email', 'phone', 'package', 'description',)
