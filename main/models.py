from django.db import models

# Create your models here.
class timeSpaceAll(models.Model):
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract= True


class carossel(timeSpaceAll):
    name=models.CharField('nom',max_length=200)
    frst_image=models.ImageField(upload_to='main/images/carossels')
    scd_image=models.ImageField(upload_to='main/images/carossels')
    trd_image=models.ImageField(upload_to='main/images/carossels')
    title_1=models.CharField('titre1',max_length=200)
    title_2=models.CharField('titre2',max_length=200)
    title_3=models.CharField('titre3', max_length=200)
    descrpt_1=models.TextField("dscrpt1",blank=True)
    descrpt_2=models.TextField("dscrpt2",blank=True)
    descrpt_3=models.TextField("dscrpt3",blank=True)

    def __str__(self):
        return self.name


class service(timeSpaceAll):
    name= models.CharField( 'Nom',max_length=200)
    descriptionBref=models.TextField(blank=True)
    description=models.TextField(blank=True)
    image= models.ImageField(upload_to='main/images/services')

    def __str__(self):
        return self.name

class formation(timeSpaceAll):
    name= models.CharField( 'Nom',max_length=200)
    descriptionBref=models.TextField(blank=True)
    description=models.TextField(blank=True)
    image= models.ImageField(upload_to='main/images/formation')

    def __str__(self):
        return self.name



class content(timeSpaceAll):
    name=models.CharField('Nom',max_length=200)
    title=models.CharField('Titre',max_length=200)
    description=models.TextField('description',blank=True)

    def __str__(self):
        return self.name
 

class home_page(timeSpaceAll):

    name=models.CharField('Nom',max_length=200)
    about_image=models.ImageField(upload_to='main/images/home_page')
    about_description=models.TextField('aboutDescription',blank=True)
    about_banniere=models.TextField('banniere',blank=True)

    def __str__(self):
        return self.name
 


class message(timeSpaceAll):
    senderName=models.CharField("Nom complet",max_length=200)
    senderEmail=models.EmailField("votre email",max_length=254)
    mainMessage=models.TextField("Ton message",blank=True)

    def __str__(self):
        return self.senderName
  
class subscriber(timeSpaceAll):
    subEmail= models.EmailField(max_length=254)