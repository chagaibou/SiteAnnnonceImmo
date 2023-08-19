from django.contrib import admin
from . import models
# Register your models here.

class DetailAnnonceAdmin(admin.ModelAdmin):
    pass

class EmplacementAdmin(admin.ModelAdmin):
    pass
class AnnonceAdmin(admin.ModelAdmin):
    pass

class AnnonceDetailsCaracteristiquesAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.AnnonceDetail,DetailAnnonceAdmin)
admin.site.register(models.Emplacement,EmplacementAdmin)
admin.site.register(models.Annonce,AnnonceAdmin)
admin.site.register(models.Caracteristiques,AnnonceDetailsCaracteristiquesAdmin)
