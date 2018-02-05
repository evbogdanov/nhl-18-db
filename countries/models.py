from django.db import models

class Country(models.Model):
    class Meta:
        verbose_name_plural = 'countries'

    abbrev = models.CharField(max_length=3, primary_key=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.abbrev
