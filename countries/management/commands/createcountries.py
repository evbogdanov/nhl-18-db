from django.core.management.base import BaseCommand
from countries.models import Country

class Command(BaseCommand):
    help = 'Creates all countries'

    def handle(self, *args, **options):
        Country.create_all()
        self.stdout.write(self.style.SUCCESS('Countries created'))
