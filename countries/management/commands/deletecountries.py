from django.core.management.base import BaseCommand
from countries.models import Country

class Command(BaseCommand):
    help = 'Deletes all countries'

    def handle(self, *args, **options):
        Country.delete_all()
        self.stdout.write(self.style.SUCCESS('Countries deleted'))
