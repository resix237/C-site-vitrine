
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from . import models
from . import forms
# Create your views here.
def index(request):
    carossel= models.carossel.objects.get(name='home')
    home_page=models.home_page.objects.get(name='home')
    formation=models.formation.objects.all()
    service=models.service.objects.all

    return render(request, "main/home.html",{'carossel':carossel, 'home_page':home_page,'formation':formation, 'service':service})

def presentation(request):
    carossel= models.carossel.objects.get(name='home')
    
    return render(request,"main/presentation.html",{'carossel':carossel } )


def services(request):
    carossel= models.carossel.objects.get(name='home')
    service=models.service.objects.all
    
    return render(request,"main/services.html",{'carossel':carossel, 'service':service } )



def formations(request):
     formation=models.formation.objects.all()
     carossel= models.carossel.objects.get(name='home')
    
     return render(request,"main/formations.html",{'carossel':carossel, 'formation':formation } )


def contact(request):
    carossel= models.carossel.objects.get(name='home')
    if request.method == "POST":
       
        full_name= request.POST['senderName']
        email= request.POST['senderEmail']
        yourText= request.POST['mainMessage']

        send_mail('contacter par '+full_name,
            ''+yourText+' Email: '+email,
            email,
            ["resix237pro@gmail.com",'marc.fouda@OFTY.fr'],
            fail_silently=False
            )
        message_form= forms.messageForm(request.POST).save()
       
        return render(request,"main/contact.html/",{'carossel':carossel,'full_name':full_name})
    else:
        message_form= forms.messageForm()
    
    return render(request,"main/contact.html",{'carossel':carossel,'message_form':message_form } )