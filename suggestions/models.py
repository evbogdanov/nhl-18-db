from django.db import models
from teams.models import Team
from players.models import Skater


def get_suggestions(name):
    classes = (
        ('team', Team),
        ('skater', Skater),
    )

    suggestions = []
    for type, cls in classes:
        objects = cls.filter_objects_by_name(name)
        if type == 'skater':
            objects = objects.order_by('-overall')
        objects = objects[:3]
        suggestions += [
            {'name': o.name, 'img': o.img, 'type': type} for o in objects
        ]
    
    return suggestions
