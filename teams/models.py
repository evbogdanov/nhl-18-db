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
    forwards_rating = models.IntegerField(default=0)
    defensemen_rating = models.IntegerField(default=0)
    goalies_rating = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    @classmethod
    def create_all(cls):
        path = os.path.join(BASE_DIR, 'db', 'teams.yml')
        with open(path) as file:
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

    @classmethod
    def set_ratings(cls):
        for team in cls.objects.all():
            forwards_ratings, forwards_count = 0, 0
            defensemen_ratings, defensemen_count = 0, 0
            # TODO: team.goalies_rating
            for skater in team.players_skaters.all():
                if skater.position == skater.DEFENSEMAN:
                    defensemen_ratings += skater.overall
                    defensemen_count += 1
                else:
                    forwards_ratings += skater.overall
                    forwards_count += 1
            if defensemen_count > 0:
                team.defensemen_rating = round(defensemen_ratings /
                                               defensemen_count)
            if forwards_count > 0:
                team.forwards_rating = round(forwards_ratings /
                                             forwards_count)
            team.save()

    @property
    def conference(self):
        if (self.division == self.ATLANTIC
        or self.division == self.METROPOLITAN):
            return 'Eastern'
        return 'Western'

    @property
    def img(self):
        return f'/static/img/team/{self.abbrev}.svg'

    @property
    def json(self):
        return {
            'abbrev': self.abbrev,
            'name': self.name,
            'country': self.country.json,
            'division': self.get_division_display(),
            'conference': self.conference,
            'is_active': self.is_active,
            'img': self.img,
            'forwards_rating': self.forwards_rating,
            'defensemen_rating': self.defensemen_rating,
            'goalies_rating': self.goalies_rating,
        }
