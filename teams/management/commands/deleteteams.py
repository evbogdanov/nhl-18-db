from django.core.management.base import BaseCommand
from teams.models import Team

class Command(BaseCommand):
    help = 'Deletes all teams'

    def handle(self, *args, **options):
        Team.delete_all()
        self.stdout.write(self.style.SUCCESS('Teams deleted'))
