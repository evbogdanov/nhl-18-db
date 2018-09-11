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

  get ratingColorClass() {
    const rating = this.skater.overall;
    return {
      'skater-list-item__overall-indicator_bg_green': rating >= 80,
      'skater-list-item__overall-indicator_bg_yellow': rating < 80,
    };
  }

  get ratingStyle() {
    const rating = this.skater.overall;
    const ratingHalf = 50;
    const ratingToDegRatio = 3.6;
    const degs = (rating - ratingHalf) * ratingToDegRatio;
    return {'transform': `rotate(${degs}deg)`};
  }

  onClick(event) {
    event.preventDefault();
    this.skaterModalService.changeSkater(this.skater);
  }
}
