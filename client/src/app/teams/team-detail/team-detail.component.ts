import { Component, OnInit } from '@angular/core';
import { Router, ActivatedRoute, ParamMap } from '@angular/router';
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
  teamNotFound: boolean = false;
  team: Team | null = null;
  skaters: Skater[] = [];

  constructor(
    private route: ActivatedRoute,
    private router: Router,
    private teamService: TeamService,
    private skaterService: SkaterService
  ) {}

  ngOnInit() {
    this.route.paramMap.subscribe((params: ParamMap) => {
      const abbrev = params.get('abbrev');
      this.teamService.getTeam(abbrev)
        .subscribe(team => {
          if (team === null) {
            this.teamNotFound = true;
          }
          this.team = team;
        });
      this.skaterService.searchSkaters({'team_abbrev': abbrev})
        .subscribe(skaters => this.skaters = skaters);
    });
  }

  get forwards() {
    return this.skaters
      .filter(s => s.position !== 'Defenseman');
  }

  get defensemen() {
    return this.skaters
      .filter(s => s.position === 'Defenseman');
  }

}
