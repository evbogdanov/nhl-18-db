import { Component, OnInit, Input } from '@angular/core';

@Component({
  selector: 'app-skater-rating',
  templateUrl: './skater-rating.component.html',
  styleUrls: ['./skater-rating.component.css']
})
export class SkaterRatingComponent implements OnInit {
  @Input() rating: number;
  @Input() isLarge: boolean;

  constructor() { }

  ngOnInit() {
  }

  get ratingColorClass() {
    return {
      'rating__indicator_bg_green': this.rating >= 80,
      'rating__indicator_bg_yellow': this.rating < 80,
    };
  }

  get ratingStyle() {
    const rating = this.rating;
    const ratingHalf = 50;
    const ratingToDegRatio = 3.6;
    const degs = (rating - ratingHalf) * ratingToDegRatio;
    return {'transform': `rotate(${degs}deg)`};
  }

}
