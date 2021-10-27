from django import forms
from django.forms import widgets
from . import models



class messageForm(forms.ModelForm):
    class Meta:
        model = models.message
        fields=('senderName','senderEmail','mainMessage',)
        widgets={
            'senderName': forms.TextInput(attrs={
               'class':'form-control',
             
            }),
            'senderEmail': forms.EmailInput(attrs={
               'class':'form-control','placeholder':"Entrer l'email",
            
            }),
            'mainMessage': forms.Textarea(attrs={
               'class':'form-control',
               
               
            }),
            
        }