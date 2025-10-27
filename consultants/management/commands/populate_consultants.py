from django.core.management.base import BaseCommand
from consultants.models import Consultant
import json
from django.conf import settings
import os

class Command(BaseCommand):
    help = 'Populate consultants depuis fixtures/consultants_fixture.json'

    def handle(self, *args, **options):
        path = os.path.join(settings.BASE_DIR, 'consultants', 'fixtures', 'consultants_fixture.json')
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        for obj in data:
            fields = obj['fields']
            Consultant.objects.update_or_create(
                nom=fields['nom'],
                defaults={
                    'domaine': fields.get('domaine', ''),
                    'experience': fields.get('experience', ''),
                    'disponibilite': fields.get('disponibilite', ''),
                    'ville': fields.get('ville', ''),
                    'lien_linkedin': fields.get('lien_linkedin', ''),
                }
            )
        self.stdout.write(self.style.SUCCESS('Consultants importés.'))
