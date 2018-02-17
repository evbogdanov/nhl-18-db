from django.db import models
from countries.models import Country
from teams.models import Team
from nhl_18_db.settings import BASE_DIR
import os
import yaml


################################################################################
### An abstract player
################################################################################

class Player(models.Model):
    class Meta:
        abstract = True

    nhlcom_id = models.IntegerField(primary_key=True)

    country = models.ForeignKey(
        Country,
        on_delete=models.CASCADE,
        related_name='%(app_label)s_%(class)ss',
    )

    team = models.ForeignKey(
        Team,
        on_delete=models.CASCADE,
        related_name='%(app_label)s_%(class)ss',
    )

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    born = models.DateField()
    number = models.IntegerField()

    salary = models.FloatField()  # TODO: consider switching to decimal
    years_left = models.IntegerField()

    height = models.IntegerField()
    weight = models.IntegerField()

    draft_team = models.ForeignKey(
        Team,
        on_delete=models.CASCADE,
        null=True,
        related_name='%(app_label)s_%(class)ss_drafted',
    )
    draft_year = models.IntegerField(null=True)
    draft_round = models.IntegerField(null=True)
    draft_overall = models.IntegerField(null=True)

    potential = models.IntegerField()
    overall = models.IntegerField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


################################################################################
### Skater
################################################################################

class Skater(Player):
    ## Position choices
    CENTER = 'c'
    DEFENSEMAN = 'd'
    LEFT_WING = 'lw'
    RIGHT_WING = 'rw'
    POSITION_CHOICES = (
        (CENTER, 'Center'),
        (DEFENSEMAN, 'Defenseman'),
        (LEFT_WING, 'Left Wing'),
        (RIGHT_WING, 'Right Wing'),
    )

    ## Type choices
    DEFENSIVE_DEFENSEMAN = 'dfd'
    GRINDER = 'grn'
    OFFENSIVE_DEFENSEMAN = 'ofd'
    PLAYMAKER = 'ply'
    POWER_FORWARD = 'pwf'
    SNIPER = 'snp'
    TWO_WAY_DEFENDERD = 'twd'
    TWO_WAY_FORWARD = 'twf'
    TYPE_CHOICES = (
        (DEFENSIVE_DEFENSEMAN, 'Defensive Defenseman'),
        (GRINDER, 'Grinder'),
        (OFFENSIVE_DEFENSEMAN, 'Offensive Defenseman'),
        (PLAYMAKER, 'Playmaker'),
        (POWER_FORWARD, 'Power Forward'),
        (SNIPER, 'Sniper'),
        (TWO_WAY_DEFENDERD, '2 Way Defender'),
        (TWO_WAY_FORWARD, '2 Way Forward'),
    )

    ## Shoots choices
    LEFT = 'l'
    RIGHT = 'r'
    SHOOTS_CHOICES = (
        (LEFT, 'Left'),
        (RIGHT, 'Right'),
    )

    ## Skater
    position = models.CharField(max_length=2, choices=POSITION_CHOICES)
    type = models.CharField(max_length=3, choices=TYPE_CHOICES)
    shoots = models.CharField(max_length=1, choices=SHOOTS_CHOICES)

    puck_skills = models.IntegerField()
    senses = models.IntegerField()
    shooting = models.IntegerField()
    defense = models.IntegerField()
    skating = models.IntegerField()
    physical = models.IntegerField()

    deking = models.IntegerField()
    hand_eye = models.IntegerField()
    passing = models.IntegerField()
    puck_control = models.IntegerField()

    discipline = models.IntegerField()
    offensive_awareness = models.IntegerField()
    poise = models.IntegerField()

    slap_shot_accuracy = models.IntegerField()
    slap_shot_power = models.IntegerField()
    wrist_shot_accuracy = models.IntegerField()
    wrist_shot_power = models.IntegerField()

    defensive_awareness = models.IntegerField()
    faceoffs = models.IntegerField()
    shot_blocking = models.IntegerField()
    stick_checking = models.IntegerField()

    acceleration = models.IntegerField()
    agility = models.IntegerField()
    balance = models.IntegerField()
    endurance = models.IntegerField()
    speed = models.IntegerField()

    aggressiveness = models.IntegerField()
    body_checking = models.IntegerField()
    durability = models.IntegerField()
    fighting_skill = models.IntegerField()
    strength = models.IntegerField()

    @classmethod
    def from_yaml(cls, data):
        data['country'] = Country.objects.get(abbrev=data['country_abbrev'])
        del data['country_abbrev']

        data['team'] = Team.objects.get(abbrev=data['team_abbrev'])
        del data['team_abbrev']

        if data['draft_team_abbrev'] is None:
            data['draft_team'] = None
        else:
            data['draft_team'] = Team.objects.get(
                abbrev=data['draft_team_abbrev']
            )
        del data['draft_team_abbrev']

        data['shoots'] = cls.LEFT if data['shoots'] == 'left' else cls.RIGHT

        for k, v in cls.TYPE_CHOICES:
            if data['type'] == v.lower():
                data['type'] = k
                break

        return cls(**data)

    @classmethod
    def create(cls, team_abbrev=None):
        teams = Team.objects.filter(is_active=True)
        if team_abbrev is not None:
            teams = teams.filter(abbrev=team_abbrev)
        for team in teams:
            team_dir = os.path.join(BASE_DIR, 'db', 'skaters', team.abbrev)
            for skater_file in os.listdir(team_dir):
                if not '.yml' in skater_file:
                    continue
                skater_path = os.path.join(team_dir, skater_file)
                skater_data = yaml.load(open(skater_path))
                skater = cls.from_yaml(skater_data)
                skater.save()

    @classmethod
    def create_all(cls):
        cls.create()

    @classmethod
    def create_for_team(cls, team_abbrev):
        cls.create(team_abbrev)

    @property
    def json(self):
        di = self.__dict__
        d = {}
        for k in di.keys():
            if not k.startswith('_'):
                d[k] = di[k]

        d['country'] = self.country.json
        del d['country_id']

        d['team'] = self.team.json
        del d['team_id']

        if d['draft_team_id'] is None:
            d['draft_team'] = None
        else:
            d['draft_team'] = self.draft_team.json
        del d['draft_team_id']

        d['position'] = self.get_position_display()
        d['type'] = self.get_type_display()
        d['shoots'] = self.get_shoots_display()

        return d


################################################################################
### Goalie
################################################################################

## TODO: class Goalie(Player)
