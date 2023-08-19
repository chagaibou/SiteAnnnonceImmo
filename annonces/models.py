from django.conf import settings
from django.db import models
from . import choices
# Create your models here.
class Caracteristiques(models.Model):
    jardin = models.BooleanField(blank=True)
    terrasse = models.BooleanField(blank=True)
    balcon = models.BooleanField(blank=True)
    meuble = models.BooleanField(blank=True)
    cuisine = models.BooleanField(blank=True)
    machine_a_laver = models.BooleanField(blank=True)

class AnnonceDetail(models.Model):
    categorie = models.CharField(max_length=255, choices=choices.CATEGORIES_CHOICES, default='appartement')
    surface = models.DecimalField(max_digits=6,decimal_places=2)
    prix = models.DecimalField(max_digits=8,decimal_places=2)
    pieces = models.IntegerField()
    salleDeBains = models.IntegerField()
    etat = models.CharField(max_length=30,choices=choices.ETAT_CHOICES)
    caracteristiques = models.OneToOneField(Caracteristiques,on_delete=models.CASCADE,default='jardin')

class Emplacement(models.Model):
    adresse = models.CharField(max_length=255)
    quartier = models.CharField(max_length=255,choices=choices.QUARTIERS_KENITRA_CHOICES)
class Annonce(models.Model):
    annonceDetail = models.OneToOneField(AnnonceDetail,on_delete=models.CASCADE,related_name="annonce",default="1")
    emplacement = models.OneToOneField(Emplacement,on_delete=models.CASCADE,related_name="annonce")
    titre = models.CharField(max_length=500)
    description = models.CharField(max_length=5000)
    image = models.ImageField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="annonce")

    def __str__(self):
        return self.titre

















