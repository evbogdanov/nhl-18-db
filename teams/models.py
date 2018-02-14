from django.db import models
from countries.models import Country
from nhl_18_db.settings import BASE_DIR
import os
import yaml


class Team(models.Model):
    ATLANTIC = 'atl'
    CENTRAL = 'cen'
    METROPOLITAN = 'met'
    PACIFIC = 'pac'
    SOUTHEAST = 'sou'
    DIVISION_CHOICES = (
        (ATLANTIC, 'Atlantic'),
        (CENTRAL, 'Central'),
        (METROPOLITAN, 'Metropolitan'),
        (PACIFIC, 'Pacific'),
        (SOUTHEAST, 'Southeast'),
    )

    abbrev = models.CharField(max_length=3, primary_key=True)
    name = models.CharField(max_length=30)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    division = models.CharField(max_length=3, choices=DIVISION_CHOICES)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    @classmethod
    def create_all(cls):
        file = open(os.path.join(BASE_DIR, 'db', 'teams.yml'))
        teams = yaml.load(file)['teams']
        for abbrev in teams:
            t = teams[abbrev]
            team = cls(
                abbrev=abbrev,
                name=t['name'],
                country=Country.objects.get(abbrev=t['country_abbrev']),
                division=t['division'],
                is_active=t['is_active'],
            )
            team.save()

    @classmethod
    def delete_all(cls):
        cls.objects.all().delete()

    @property
    def conference(self):
        if (self.division == self.ATLANTIC
        or self.division == self.METROPOLITAN):
            return 'Eastern'
        return 'Western'

    @property
    def json(self):
        return {
            'abbrev': self.abbrev,
            'name': self.name,
            'country': self.country.json,
            'division': self.get_division_display(),
            'conference': self.conference,
            'is_active': self.is_active,
        }
