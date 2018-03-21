import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { Team } from '../team.model';
import { TeamService } from '../team.service';
import { Skater } from '../../skaters/skater.model';
import { SkaterService } from '../../skaters/skater.service';


@Component({
  selector: 'app-team-detail',
  templateUrl: './team-detail.component.html',
  styleUrls: ['./team-detail.component.css']
})
export class TeamDetailComponent implements OnInit {
  team: Team | null = null;
  skaters: Skater[] = [];

  constructor(private route: ActivatedRoute,
              private teamService: TeamService,
              private skaterService: SkaterService) {}

  ngOnInit() {
    const abbrev = this.route.snapshot.paramMap.get('abbrev');
    this.teamService.getTeam(abbrev)
      .subscribe(team => this.team = team);
    this.skaterService.searchSkaters({'team_abbrev': abbrev})
      .subscribe(skaters => this.skaters = skaters);
  }

}
