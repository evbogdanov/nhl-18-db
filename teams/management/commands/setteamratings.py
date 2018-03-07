from django.core.management.base import BaseCommand
from teams.models import Team

class Command(BaseCommand):
    help = 'Set team ratings'

    def handle(self, *args, **options):
        Team.set_ratings()
        self.stdout.write(self.style.SUCCESS('Ratings set'))
