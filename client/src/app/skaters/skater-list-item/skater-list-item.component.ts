import { Component, OnInit, Input } from '@angular/core';
import { Skater } from '../skater.model';
import { SkaterModalService } from '../skater-modal.service';


@Component({
  selector: 'app-skater-list-item',
  templateUrl: './skater-list-item.component.html',
  styleUrls: ['./skater-list-item.component.css']
})
export class SkaterListItemComponent implements OnInit {
  @Input() skater: Skater;

  constructor(private skaterModalService: SkaterModalService) { }

  ngOnInit() {
  }

  onClick(event) {
    event.preventDefault();
    this.skaterModalService.changeSkater(this.skater);
  }
}
