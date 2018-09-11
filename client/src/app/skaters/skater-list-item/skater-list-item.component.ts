import { Component, OnInit, Input } from '@angular/core';
import { Skater } from '../skater.model';


@Component({
  selector: 'app-skater-list-item',
  templateUrl: './skater-list-item.component.html',
  styleUrls: ['./skater-list-item.component.css']
})
export class SkaterListItemComponent implements OnInit {
  @Input() skater: Skater;

  constructor() { }

  ngOnInit() {
  }

  get ratingColorClass {
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
}
