from django.shortcuts import render
from .models import Consultant

def dashboard(request):
    date_filtre = request.GET.get('disponibilite_date')
    consultants = Consultant.objects.all()

    if date_filtre:
        consultants = consultants.filter(disponibilite_date__lte=date_filtre)

    return render(request, "consultants/dashboard.html", {
        "consultants": consultants,
        "date_filtre": date_filtre
    })

