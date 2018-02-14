from django.db import models
from nhl_18_db.settings import BASE_DIR
import os
import yaml


class Country(models.Model):
    class Meta:
        verbose_name_plural = 'countries'

    abbrev = models.CharField(max_length=3, primary_key=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    @classmethod
    def create_all(cls):
        file = open(os.path.join(BASE_DIR, 'db', 'countries.yml'))
        data = yaml.load(file)['countries'].items()
        for abbrev, name in data:
            country = cls(abbrev=abbrev, name=name)
            country.save()

    @classmethod
    def delete_all(cls):
        cls.objects.all().delete()

    @property
    def json(self):
        return {
            'abbrev': self.abbrev,
            'name': self.name,
        }
