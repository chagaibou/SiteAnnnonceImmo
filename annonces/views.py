from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from . import forms
from .models import Annonce
# Create your views here.

def home(request):
    annonces = Annonce.objects.all()

    return render(request,'annonces/home.html',context={'annonces':annonces})

@login_required
def publier_annonce(request):
    annonceForm = forms.AnnonceForm()
    annonceDetailForm = forms.AnnonceDetailForm()
    emplacementForm = forms.EmplacementForm()
    caracteristiquesForm = forms.AnnonceCaracteristiquesForm()
    if request.method == 'POST':
        annonceForm = forms.AnnonceForm(request.POST,request.FILES)
        annonceDetailForm = forms.AnnonceDetailForm(request.POST)
        emplacementForm = forms.EmplacementForm(request.POST)
        caracteristiquesForm = forms.AnnonceCaracteristiquesForm(request.POST)
        if all([annonceDetailForm.is_valid(),caracteristiquesForm.is_valid(),emplacementForm.is_valid(),annonceForm.is_valid()]):
            caracteristiques = caracteristiquesForm.save()
            annonceDetail = annonceDetailForm.save(commit=False)
            annonceDetail.caracteristiques = caracteristiques
            annonceDetail.save()
            emplacement = emplacementForm.save()
            annonce = annonceForm.save(commit=False)
            annonce.annonceDetail = annonceDetail
            annonce.emplacement = emplacement
            annonce.user = request.user
            annonce.save()
            return redirect('home')

    context = {
        'annonceForm' : annonceForm,
        'annonceDetailForm' : annonceDetailForm,
        'emplacementForm' : emplacementForm,
        'caracteristiquesForm' : caracteristiquesForm,
    }

    return render(request,'annonces/publier_annonce.html',context=context)

def annonce_detail(request,annonce_id):
        annonce = get_object_or_404(Annonce,id=annonce_id)
        return render(request,'annonces/annonce_detail.html',context={'annonce':annonce})