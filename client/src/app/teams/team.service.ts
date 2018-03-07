import { Injectable } from '@angular/core';
import { Team } from './team.model';

const MOCK_TEAMS: Team[] = [
  {
    "abbrev": "ana",
    "name": "Anaheim Ducks",
    "country": {
      "abbrev": "usa",
      "name": "USA"
    },
    "division": "Pacific",
    "conference": "Western",
    "is_active": true,
    "img": "/static/img/team/ana.svg",
    "forwards_rating": 82,
    "defensemen_rating": 81,
    "goalies_rating": 0
  },
  {
    "abbrev": "ari",
    "name": "Arizona Coyotes",
    "country": {
      "abbrev": "usa",
      "name": "USA"
    },
    "division": "Pacific",
    "conference": "Western",
    "is_active": true,
    "img": "/static/img/team/ari.svg",
    "forwards_rating": 78,
    "defensemen_rating": 81,
    "goalies_rating": 0
  }
];

@Injectable()
export class TeamService {
  getTeams(): Team[] {
    // TODO: fetch teams from the server
    return MOCK_TEAMS;
  }
}
