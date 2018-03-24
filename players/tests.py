from django.test import TestCase
from countries.models import Country
from teams.models import Team
from .models import Skater

class SkaterTestCase(TestCase):
    N_PENGUINS = 21
    MALKIN_ID = 8471215

    @classmethod
    def setUpClass(cls):
        Country.create_all()
        Team.create_all()
        Skater.create_for_team('pit')

    @classmethod
    def tearDownClass(cls):
        pass

    def test_skaters_created(self):
        """All testing skaters are created"""
        self.assertEqual(Skater.objects.count(), self.N_PENGUINS)

    def test_skaters_belong_to_team(self):
        """Skaters belong to their team"""
        team = Team.objects.get(abbrev='pit')
        self.assertEqual(team.players_skaters.count(), self.N_PENGUINS)

    def test_skaters_drafted_by_team(self):
        """Skaters are drafted by their team"""
        team = Team.objects.get(abbrev='pit')
        skater = team.players_skaters_drafted.get(nhlcom_id=self.MALKIN_ID)
        self.assertEqual(skater.last_name, 'Malkin')

    def test_skater_as_string(self):
        """Skater to string"""
        s = Skater.objects.get(nhlcom_id=self.MALKIN_ID)
        self.assertEqual(f'{s}', 'Evgeni Malkin')

    def test_skater_as_dict(self):
        """Skater to dict"""
        s = Skater.objects.get(nhlcom_id=self.MALKIN_ID)
        d = s.as_dict()
        self.assertEqual(d['last_name'], 'Malkin')

    def test_skater_as_json(self):
        """Skater to JSON"""
        s = Skater.objects.get(nhlcom_id=self.MALKIN_ID)
        self.assertEqual(s.json['first_name'], 'Evgeni')
        self.assertEqual(s.json['country']['name'], 'Russia')
        self.assertEqual(s.json['team']['country']['name'], 'USA')

    def test_skater_age(self):
        """How old are you, skater?"""
        s = Skater.objects.get(nhlcom_id=self.MALKIN_ID)
        self.assertEqual(s.age, 31)

    def test_skater_fields(self):
        """Access to skater's fields"""
        fields = Skater.get_fields()
        self.assertTrue('nhlcom_id' in fields)
        self.assertTrue('country' in fields)
        self.assertTrue('team' in fields)

    def test_search_default_ordering(self):
        """Skaters are sorted by overall rating""" 
        skaters = Skater.search({})
        self.assertEqual(skaters[0]['last_name'], 'Crosby')
        self.assertEqual(skaters[-1]['last_name'], 'Sprong')

    def test_search_custom_ordering(self):
        """Skaters can be ordered by custom field"""
        skaters = Skater.search({'order_by': 'faceoffs'})
        self.assertEqual(skaters[0]['faceoffs'], 50)
        self.assertEqual(skaters[-1]['faceoffs'], 80)

    def test_search_custom_ordering_descending(self):
        """Search and sort skaters in reversed order"""
        skaters = Skater.search({'order_by': 'faceoffs', 'desc': True})
        self.assertEqual(skaters[0]['faceoffs'], 80)
        self.assertEqual(skaters[-1]['faceoffs'], 50)

    def test_search_by_country(self):
        """Skaters are searchable by country"""
        malkin = Skater.search({'country_abbrev': 'rus'})[0]
        self.assertEqual(malkin['number'], 71)

    def test_search_by_team(self):
        """Skaters are searchable by team"""
        self.assertEqual(len(Skater.search({'team_abbrev': 'pit'})), self.N_PENGUINS)
        self.assertEqual(len(Skater.search({'team_abbrev': 'wtf'})), 0)

    def test_search_by_first_name(self):
        """Search skaters by first name"""
        self.assertEqual(Skater.search({'name': 'evge'})[0]['first_name'], 'Evgeni')

    def test_search_by_last_name(self):
        """Search skaters by last name"""
        self.assertEqual(Skater.search({'name': 'malk'})[0]['last_name'], 'Malkin')

    def test_search_by_full_name(self):
        """Search skaters by full first_name and partial last_name"""
        self.assertEqual(Skater.search({'name': 'evgeni ma'})[0]['last_name'], 'Malkin')

    def test_search_by_age(self):
        """Search skaters by age"""
        skaters = Skater.search({'age_from': 30, 'age_to': 30})
        self.assertEqual(skaters[0]['age'], 30)
        self.assertEqual(skaters[-1]['age'], 30)

    def test_search_by_something_exact(self):
        """Search skaters by some exact fields"""
        skaters = Skater.search({'position': 'rw', 'type': 'grn', 'shoots': 'r'})
        self.assertEqual(skaters[0]['last_name'], 'Reaves')
        self.assertEqual(skaters[-1]['last_name'], 'Reaves')

    def test_search_by_something_in_range(self):
        """Search skaters by something in range"""
        ## Potential
        skaters = Skater.search({'potential_from': 4, 'potential_to': 4})
        self.assertEqual(skaters[0]['number'], 87)
        self.assertEqual(skaters[-1]['number'], 71)
        ## Acceleration
        skaters = Skater.search({'acceleration_from': 90})
        self.assertEqual(skaters[0]['last_name'], 'Crosby')
        self.assertEqual(skaters[-1]['last_name'], 'Kessel')
