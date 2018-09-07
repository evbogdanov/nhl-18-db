import { Component, AfterViewInit, OnDestroy, ViewChild } from '@angular/core';
import { Renderer2 } from '@angular/core';

@Component({
  selector: 'app-teams-list-skel',
  templateUrl: './teams-list-skel.component.html',
  styleUrls: ['./teams-list-skel.component.css']
})
export class TeamsListSkelComponent implements AfterViewInit, OnDestroy {
  interval: any;
  glowPosition = 'left';

  @ViewChild('glow') glow;

  constructor(private renderer: Renderer2) { }

  tick() {
    let left: string;
    if (this.glowPosition === 'left') {
      left = '100%';
      this.renderer.setStyle(this.glow.nativeElement, 'transition', 'left .5s linear');
      this.glowPosition = 'right';
    }
    else {
      const glowWidth = this.glow.nativeElement.clientWidth;
      left = `-${glowWidth}px`;
      this.renderer.setStyle(this.glow.nativeElement, 'transition', 'none');
      this.glowPosition = 'left';
    }
    this.renderer.setStyle(this.glow.nativeElement, 'left', left);
  }

  ngAfterViewInit() {
    this.interval = setInterval(() => this.tick(), 500);
  }

  ngOnDestroy() {
    clearInterval(this.interval);
  }
}
