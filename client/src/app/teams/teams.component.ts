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
    new Team(
      'pit',
      'Pittsburgh Penguins',
      new Country('usa', 'USA'),
      'Eastern',
      'Metropolitan',
    ),
    new Team(
      'nsh',
      'Nashville Predators',
      new Country('usa', 'USA'),
      'Western',
      'Central',
    )
  ];
}
