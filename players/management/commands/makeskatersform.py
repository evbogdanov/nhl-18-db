from django.core.management.base import BaseCommand
from nhl_18_db.settings import BASE_DIR
from players.models import Skater
import json
import os


class Command(BaseCommand):
    help = 'Makes skaters form used on front end'

    def handle(self, *args, **options):
        out = '''//
// This file is generated on back end
//
// See:
//   - players/models.py
//   - players/management/commands/makeskatersform.py
//
// To sync form fields, run `python manage.py makeskatersform`
//
export const FORM_FIELDS = '''

        form_fields = Skater.make_form_fields()
        form_as_json = json.dumps(form_fields)
        out += form_as_json

        path = os.path.join(BASE_DIR,
                            'client', 'src', 'app', 'skaters',
                            'skaters.form.ts')
        with open(path, 'w') as file:
            file.write(out)

        self.stdout.write(self.style.SUCCESS('Form made'))
