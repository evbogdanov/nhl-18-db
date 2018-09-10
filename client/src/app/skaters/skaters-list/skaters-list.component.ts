import { Component, OnInit, Input } from '@angular/core';
import { Skater } from '../skater.model';

@Component({
  selector: 'app-skaters-list',
  templateUrl: './skaters-list.component.html',
  styleUrls: ['./skaters-list.component.css']
})
export class SkatersListComponent implements OnInit {
  @Input() skaters: Skater[];

  constructor() { }

  ngOnInit() {
  }

}
