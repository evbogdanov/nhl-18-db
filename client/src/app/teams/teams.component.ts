import { Component, OnInit } from '@angular/core';
import { Team } from './team.model'
import { Country } from '../countries/country.model'

@Component({
  selector: 'app-teams',
  templateUrl: './teams.component.html',
  styleUrls: ['./teams.component.css']
})
export class TeamsComponent {
  teams: Team[] = [
    {
      "abbrev": "wsh",
      "name": "Washington Capitals",
      "country": {
        "abbrev": "usa",
        "name": "USA"
      },
      "division": "Metropolitan",
      "conference": "Eastern",
      "is_active": true,
      "img": "/static/img/team/wsh.svg"
    },
    {
      "abbrev": "atl",
      "name": "Atlanta Thrashers",
      "country": {
        "abbrev": "usa",
        "name": "USA"
      },
      "division": "Southeast",
      "conference": "Western",
      "is_active": false,
      "img": "/static/img/team/atl.svg"
    }
  ].filter(t => t.is_active)
}
