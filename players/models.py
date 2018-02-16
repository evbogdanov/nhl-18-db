from django.db import models
from countries.models import Country
from teams.models import Team


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
        related_name='%(app_label)s_%(class)s',
    )

    team = models.ForeignKey(
        Team,
        on_delete=models.CASCADE,
        related_name='%(app_label)s_%(class)s',
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
        related_name='%(app_label)s_%(class)s_drafted',
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


################################################################################
### Goalie
################################################################################

## TODO: class Goalie(Player)