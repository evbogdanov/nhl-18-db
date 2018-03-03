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
  teams: Team[];

  getTeams() {
    this.teams = this.teamService.getTeams().filter(t => t.is_active);
  }

  constructor(private teamService: TeamService) {}
  
  ngOnInit() {
    this.getTeams();
  }
}
