import { Component, OnInit } from '@angular/core';
import { Country } from '../countries/country.model'
import { Team } from './team.model'
import { TeamService } from './team.service';

@Component({
  selector: 'app-teams',
  templateUrl: './teams.component.html',
  styleUrls: ['./teams.component.css']
})
export class TeamsComponent implements OnInit {
  teams: Team[] = [];

  getTeams() {
    this.teamService.getTeams()
      .subscribe((teams) => {
        this.teams = teams.filter(t => t.is_active);
      });
  }

  constructor(private teamService: TeamService) {}
  
  ngOnInit() {
    this.getTeams();
  }

  get pacificTeams() {
    return this.teams
      .filter(t => t.division === 'Pacific');
  }

  get centralTeams() {
    return this.teams
      .filter(t => t.division === 'Central');
  }

  get metropolitanTeams() {
    return this.teams
      .filter(t => t.division === 'Metropolitan');
  }

  get atlanticTeams() {
    return this.teams
      .filter(t => t.division === 'Atlantic');
  }

}
