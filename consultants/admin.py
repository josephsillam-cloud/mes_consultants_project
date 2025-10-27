from django.contrib import admin
from .models import Consultant

@admin.register(Consultant)
class ConsultantAdmin(admin.ModelAdmin):
    list_display = ('nom', 'domaine', 'disponibilite', 'disponibilite_date', 'ville')
    list_filter = ('domaine', 'disponibilite_date')  # ← filtre par date
    search_fields = ('nom', 'domaine', 'ville')
