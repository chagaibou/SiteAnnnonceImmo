from django import forms
from . import models

class AnnonceDetailForm(forms.ModelForm):
    class Meta:
        model = models.AnnonceDetail
        fields = ['categorie','surface','prix','pieces','salleDeBains','etat']

class AnnonceCaracteristiquesForm(forms.ModelForm):
    class Meta:
        model = models.Caracteristiques
        fields = ['jardin','terrasse','balcon','meuble','cuisine','machine_a_laver']

class EmplacementForm(forms.ModelForm):
    class Meta:
        model = models.Emplacement
        fields = ['adresse','quartier']
class AnnonceForm(forms.ModelForm):
    class Meta:
        model = models.Annonce
        fields = ['titre','description','image']

