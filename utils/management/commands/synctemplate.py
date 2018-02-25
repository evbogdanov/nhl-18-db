from django.core.management.base import BaseCommand
from nhl_18_db.settings import BASE_DIR
import os
import re


def modify_html(html):
    """Point all relative paths to the bundle directory"""
    def modify_attr(attr):
        nonlocal html
        html = re.sub(
            r'(?<=' + attr + '=")(?!/)',
            '/static/bundle/',
            html
        )
    modify_attr('src')
    modify_attr('href')
    return html


class Command(BaseCommand):
    help = 'Syncs Django template with Angular template'

    def handle(self, *args, **options):
        path_in = os.path.join(BASE_DIR, 'nhl_18_db', 'static', 'bundle', 'index.html')
        with open(path_in) as file_in:
            html = file_in.read()
            html = modify_html(html)

        path_out = os.path.join(BASE_DIR, 'templates', 'index.html')
        with open(path_out, 'w') as file_out:
            file_out.write(html)

        self.stdout.write(self.style.SUCCESS('Template synced'))
