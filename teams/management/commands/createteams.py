from django.core.management.base import BaseCommand
from teams.models import Team

class Command(BaseCommand):
    help = 'Creates all teams'

    def handle(self, *args, **options):
        Team.create_all()
        self.stdout.write(self.style.SUCCESS('Teams created'))
