import { Component, OnInit, Input } from '@angular/core';
import { Skater } from '../../skaters/skater.model';


@Component({
  selector: 'app-team-skater',
  templateUrl: './team-skater.component.html',
  styleUrls: ['./team-skater.component.css']
})
export class TeamSkaterComponent implements OnInit {
  @Input() skater: Skater;
  @Input() isForward: boolean;

  constructor() { }

  ngOnInit() {
  }

}
