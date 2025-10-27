import csv
import os
from django.core.management.base import BaseCommand
from consultants.models import Consultant
from django.conf import settings

class Command(BaseCommand):
    help = "Importe des consultants à partir d'un fichier CSV"

    def add_arguments(self, parser):
        parser.add_argument(
            '--path',
            type=str,
            default=os.path.join(settings.BASE_DIR, 'consultants', 'fixtures', 'consultants_test.csv'),
            help="Chemin du fichier CSV"
        )

    def handle(self, *args, **options):
        path = options['path']
        if not os.path.exists(path):
            self.stderr.write(self.style.ERROR(f"Fichier introuvable: {path}"))
            return

        with open(path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            count = 0
            for row in reader:
                Consultant.objects.update_or_create(
                    nom = (row.get('Nom') or '').strip(),
                    defaults={
                        'domaine': (row.get('Domaine') or '').strip(),
                        'experience': (row.get('Expérience') or '').strip(),
                        'disponibilite': (row.get('Disponibilité') or '').strip(),
                        'ville': (row.get('Ville') or '').strip(),
                        'lien_linkedin': (row.get('Lien LinkedIn') or '').strip(),

                    }
                )
                count += 1

        self.stdout.write(self.style.SUCCESS(f"{count} consultants importés depuis {path}"))
