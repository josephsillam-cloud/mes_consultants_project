from django.db import models

class Consultant(models.Model):
    nom = models.CharField(max_length=100)
    domaine = models.CharField(max_length=100)
    experience = models.TextField()
    disponibilite = models.CharField(max_length=100)
    disponibilite_date = models.DateField(null=True, blank=True)  # ← nouveau champ
    ville = models.CharField(max_length=100, blank=True)
    lien_linkedin = models.URLField(blank=True)
    cv = models.FileField(upload_to='cv/', null=True, blank=True)  # ← champ PDF joint

    def __str__(self):
        return self.nom
