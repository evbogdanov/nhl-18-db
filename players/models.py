from django.db import models
from countries.models import Country
from teams.models import Team
from nhl_18_db.settings import BASE_DIR
import os
from datetime import date
import yaml

################################################################################
### An abstract player
################################################################################

class Player(models.Model):
    class Meta:
        abstract = True

    # Age is relative to 2018 (the year of the game)
    GAME_DATE = date(2018, 1, 1)

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

    ## Fields to filter
    FILTERABLE_EXACT = [
        'position',
        'shoots',
        'type',
    ]
    FILTERABLE_RANGES = [
        'acceleration',
        'aggressiveness',
        'agility',
        'balance',
        'body_checking',
        'defense',
        'defensive_awareness',
        'deking',
        'discipline',
        'durability',
        'endurance',
        'faceoffs',
        'fighting_skill',
        'hand_eye',
        'height',
        'offensive_awareness',
        'overall',
        'passing',
        'physical',
        'poise',
        'potential',
        'puck_control',
        'puck_skills',
        'salary',
        'senses',
        'shooting',
        'shot_blocking',
        'skating',
        'slap_shot_accuracy',
        'slap_shot_power',
        'speed',
        'stick_checking',
        'strength',
        'weight',
        'wrist_shot_accuracy',
        'wrist_shot_power',
        'years_left',
    ]

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

    @classmethod
    def filter_exact(cls, q, f, field):
        if q.get(field) is not None:
            f[field] = q.get(field)

    @classmethod
    def filter_range(cls, q, f, field):
        if q.get(f'{field}_from') is not None:
            f[f'{field}__gte'] = q.get(f'{field}_from')
        if q.get(f'{field}_to') is not None:
            f[f'{field}__lte'] = q.get(f'{field}_to')

    @classmethod
    def filter_by_country(cls, q, f):
        if q.get('country_abbrev') is not None:
            f['country__abbrev'] = q.get('country_abbrev')

    @classmethod
    def filter_by_team(cls, q, f):
        if q.get('team_abbrev') is not None:
            f['team__abbrev'] = q.get('team_abbrev')

    @classmethod
    def filter_by_last_name(cls, q, f):
        if q.get('last_name') is not None:
            f['last_name__istartswith'] = q.get('last_name')

    @classmethod
    def filter_by_age(cls, q, f):
        if q.get('age_from') is not None:
            f['born__lte'] = date(
                cls.GAME_DATE.year - int(q.get('age_from')),
                cls.GAME_DATE.month,
                cls.GAME_DATE.day,
            )
        if q.get('age_to') is not None:
            f['born__gte'] = date(
                cls.GAME_DATE.year - int(q.get('age_to')) - 1,
                cls.GAME_DATE.month,
                cls.GAME_DATE.day,
            )

    @classmethod
    def search(cls, q):
        # q is QueryDict
        # f is filters
        f = {}

        cls.filter_by_country(q, f)
        cls.filter_by_team(q, f)
        cls.filter_by_last_name(q, f)
        cls.filter_by_age(q, f)

        for field in cls.FILTERABLE_EXACT:
            cls.filter_exact(q, f, field)
        
        for field in cls.FILTERABLE_RANGES:
            cls.filter_range(q, f, field)

        # TODO:
        # - order
        # - pagination

        skaters = cls.objects.filter(**f)[:10]        
        return [s.json for s in skaters]

    @property
    def age(self):
        years = self.GAME_DATE.year - self.born.year
        if ((self.GAME_DATE.month, self.GAME_DATE.day) <
            (self.born.month, self.born.day)):
            return years - 1
        return years

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

        d['age'] = self.age

        return d


################################################################################
### Goalie
################################################################################

## TODO: class Goalie(Player)
