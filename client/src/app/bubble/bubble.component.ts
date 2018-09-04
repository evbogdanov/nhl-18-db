import { Component, OnInit, Input } from '@angular/core';

@Component({
  selector: 'app-bubble',
  templateUrl: './bubble.component.html',
  styleUrls: ['./bubble.component.css']
})
export class BubbleComponent implements OnInit {
  @Input() message: string;

  constructor() { }

  ngOnInit() {
  }

}
