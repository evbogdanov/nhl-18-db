from django.db import models
from teams.models import Team
from players.models import Skater


def get_suggestions(name):
    classes = (
        ('teams', Team),
        ('skaters', Skater),
    )

    suggestions = {}
    for cls_plural_name, cls in classes:
        objects = cls.filter_objects_by_name(name)
        if cls_plural_name == 'skaters':
            objects = objects.order_by('-overall')
        objects = objects[:3]
        suggestions[cls_plural_name] = [
            {'name': o.name, 'img': o.img} for o in objects
        ]
    
    return suggestions
