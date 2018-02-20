from django.core.management.base import BaseCommand
from players.models import Skater

class Command(BaseCommand):
    help = 'Deletes all skaters'

    def handle(self, *args, **options):
        Skater.delete_all()
        self.stdout.write(self.style.SUCCESS('Skaters deleted'))
