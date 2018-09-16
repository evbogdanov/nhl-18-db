import { Component, OnInit, Input } from '@angular/core';
import { Skater } from '../skater.model';
import { SkaterModalService } from '../skater-modal.service';


@Component({
  selector: 'app-skater-detail',
  templateUrl: './skater-detail.component.html',
  styleUrls: ['./skater-detail.component.css']
})
export class SkaterDetailComponent implements OnInit {
  @Input() skater: null|Skater;

  constructor(private skaterModalService: SkaterModalService) { }

  ngOnInit() {
  }

  onTeamClick() {
    // Close modal by setting its skater to null
    this.skaterModalService.changeSkater(null);
  }

}
