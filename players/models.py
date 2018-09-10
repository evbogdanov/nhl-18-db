from countries.models import Country
from datetime import date
from django.db import models
from nhl_18_db.settings import BASE_DIR
from teams.models import Team
import os
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
        return self.name

    @property
    def id(self):
        return self.nhlcom_id

    @property
    def name(self):
        return f'{self.first_name} {self.last_name}'

    @property
    def age(self):
        years = self.GAME_DATE.year - self.born.year
        if ((self.GAME_DATE.month, self.GAME_DATE.day) <
            (self.born.month, self.born.day)):
            return years - 1
        return years

    @property
    def img(self):
        return f'https://nhl.bamcontent.com/images/headshots/current/168x168/{self.nhlcom_id}@2x.jpg'


################################################################################
### Skater
################################################################################

class Skater(Player):
    ## Ages
    MIN_AGE = 18
    MAX_AGE = 45

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
    FILTERABLE_FIELDS = [
        'position',
        'shoots',
        'type',
    ]
    FILTERABLE_FIELDS_RANGES = [
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

    ## Display potential
    POTENTIALS = {
        1: 'HIGH Franchise',
        2: 'MED Franchise',
        3: 'LOW Franchise',
        4: 'EXACT Franchise',
        5: 'HIGH Elite',
        6: 'MED Elite',
        7: 'LOW Elite',
        8: 'EXACT Elite',
        9: 'HIGH Top 6 F',
        10: 'MED Top 6 F',
        11: 'LOW Top 6 F',
        12: 'EXACT Top 6 F',
        13: 'HIGH Top 4 D',
        14: 'MED Top 4 D',
        15: 'LOW Top 4 D',
        16: 'EXACT Top 4 D',
        17: 'HIGH Top 9 F',
        18: 'MED Top 9 F',
        19: 'LOW Top 9 F',
        20: 'EXACT Top 9 F',
        21: 'HIGH Top 6 D',
        22: 'MED Top 6 D',
        23: 'LOW Top 6 D',
        24: 'EXACT Top 6 D',
        25: 'HIGH Bottom 6 F',
        26: 'MED Bottom 6 F',
        27: 'LOW Bottom 6 F',
        28: 'EXACT Bottom 6 F',
        29: 'HIGH 7th D',
        30: 'MED 7th D',
        31: 'LOW 7th D',
        32: 'EXACT 7th D',
        33: 'HIGH AHL',
        34: 'MED AHL',
        35: 'LOW AHL',
        36: 'EXACT AHL',
    }

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
                with open(skater_path) as file:
                    skater_data = yaml.load(file)
                    skater = cls.from_yaml(skater_data)
                    skater.save()

    @classmethod
    def create_all(cls):
        cls.create()

    @classmethod
    def create_for_team(cls, team_abbrev):
        cls.create(team_abbrev)

    @classmethod
    def delete_all(cls):
        cls.objects.all().delete()

    @classmethod
    def filter_by(cls, field, q, f):
        if q.get(field) is not None:
            f[field] = q.get(field)

    @classmethod
    def filter_in_range_by(cls, field, q, f):
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
    def get_fields(cls):
        return [f.name for f in cls._meta.fields]

    @classmethod
    def filter_objects_by_name(cls, name):
        if ' ' in name:
            name_parts = name.split()
            if len(name_parts) == 1:
                name = name_parts[0]
            elif len(name_parts) == 2:
                first_name, last_name = name_parts
                return (cls.objects.filter(first_name__iexact=first_name) &
                        cls.objects.filter(last_name__istartswith=last_name))
        return (cls.objects.filter(first_name__istartswith=name) |
                cls.objects.filter(last_name__istartswith=name))

    @classmethod
    def filter_by_name(cls, q):
        name = q.get('name')
        if name is None:
            return cls.objects.filter()
        return cls.filter_objects_by_name(name)

    @classmethod
    def order_by(cls, q, skaters):
        field = q.get('order_by')
        sorting_field = '-overall'
        if field in cls.get_fields():
            desc = '' if q.get('desc') is None else '-'
            sorting_field = f'{desc}{field}'
        return skaters.order_by(sorting_field, 'first_name', 'last_name')

    @classmethod
    def get_pagination(cls, q, counter):
        """Return pagination info"""
        per_page = 80

        try:
            page = int(q.get('page'))
            if page < 0:
                page = 0
        except (ValueError, TypeError):
            page = 0

        pages = counter // per_page
        if counter % per_page != 0:
            pages += 1

        return {
            'start': page * per_page,
            'end': (page+1) * per_page,
            'per_page': per_page,
            'pages': pages,
            'page': page,
        }

    @classmethod
    def search(cls, q):
        # q is QueryDict
        # f is filters
        f = {}

        cls.filter_by_country(q, f)
        cls.filter_by_team(q, f)
        cls.filter_by_age(q, f)

        for field in cls.FILTERABLE_FIELDS:
            cls.filter_by(field, q, f)

        for field in cls.FILTERABLE_FIELDS_RANGES:
            cls.filter_in_range_by(field, q, f)

        skaters = cls.objects.filter(**f) & (cls.filter_by_name(q))
        skaters = cls.order_by(q, skaters)

        # Pagination
        counter = skaters.count()
        pagination = cls.get_pagination(q, counter)

        skaters = skaters[pagination['start']:pagination['end']]
        return {
            'skaters': [s.json for s in skaters],
            'pagination': pagination,
        }

    def as_dict(self):
        di = self.__dict__
        d = {}
        for k in di.keys():
            if not k.startswith('_'):
                d[k] = di[k]
        return d

    @property
    def potential_display(self):
        return self.POTENTIALS[self.potential]

    @property
    def json(self):
        d = self.as_dict()

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

        d['potential'] = self.potential_display

        d['img'] = self.img

        return d

    @classmethod
    def make_form_field_country_or_team(cls, what):
        if what == 'country':
            objects = Country.objects.all()
        else:
            objects = Team.objects.filter(is_active=True)
        return {
            'name': f'{what}_abbrev',
            'label': what.capitalize(),
            'type': 'select',
            'options': [
                {'value': obj.abbrev, 'label': obj.name} for obj in objects
            ],
        }

    @classmethod
    def make_form_field_age(cls, which):
        options = []
        for age in range(cls.MIN_AGE, cls.MAX_AGE + 1):
            options.append({'value': age, 'label': age})
        return {
            'name': f'age_{which}',
            'label': f'Age {which.capitalize()}',
            'type': 'select',
            'options': options,
        }

    @classmethod
    def make_form_field_choices(cls, name, choices):
        options = []
        for value, label in choices:
            options.append({'value': value, 'label': label})
        return {
            'name': name,
            'label': name.capitalize(),
            'type': 'select',
            'options': options,
        }

    @classmethod
    def make_form_fields(cls):
        """Fields for Angular skaters form"""
        form_fields = [
            {
                'name': 'name',
                'label': 'Name',
                'type': 'text',
            },
            cls.make_form_field_age('from'),
            cls.make_form_field_age('to'),
            cls.make_form_field_country_or_team('country'),
            cls.make_form_field_country_or_team('team'),
            cls.make_form_field_choices('position', cls.POSITION_CHOICES),
        ]

        # Default option for <select>
        for field in form_fields:
            if field['type'] == 'select':
                default_option = {'value': None,
                                  'label': ''}
                if field['name'] == 'age_from' or field['name'] == 'age_to':
                    default_option['label'] = field['label'][4:]
                field['options'].insert(0, default_option)

        return form_fields


################################################################################
### Goalie
################################################################################

## TODO: class Goalie(Player)
# POTENTIALS = {
#     1: 'HIGH Franchise',
#     2: 'MED Franchise',
#     3: 'LOW Franchise',
#     4: 'EXACT Franchise',
#     5: 'HIGH Elite',
#     6: 'MED Elite',
#     7: 'LOW Elite',
#     8: 'EXACT Elite',
#     9: 'HIGH Starter',
#     10: 'MED Starter',
#     11: 'LOW Starter',
#     12: 'EXACT Starter',
#     13: 'HIGH Fringe Starter',
#     14: 'MED Fringe Starter',
#     15: 'LOW Fringe Starter',
#     16: 'EXACT Fringe Starter',
#     17: 'HIGH Backup',
#     18: 'MED Backup',
#     19: 'LOW Backup',
#     20: 'EXACT Backup',
#     21: 'HIGH AHL',
#     22: 'MED AHL',
#     23: 'LOW AHL',
#     24: 'EXACT AHL',
# }
