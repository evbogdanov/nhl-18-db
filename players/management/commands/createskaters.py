from django.core.management.base import BaseCommand
from players.models import Skater

class Command(BaseCommand):
    help = 'Creates all skaters'

    def handle(self, *args, **options):
        Skater.create_all()
        self.stdout.write(self.style.SUCCESS('Skaters created'))
