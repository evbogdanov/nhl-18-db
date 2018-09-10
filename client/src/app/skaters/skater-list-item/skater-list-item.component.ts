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

}
