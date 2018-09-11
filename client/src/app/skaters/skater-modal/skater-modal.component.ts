import { Component, OnInit, OnDestroy } from '@angular/core';
import { Skater } from '../skater.model';
import { SkaterModalService } from '../skater-modal.service';
import { Subscription } from 'rxjs/Subscription';


@Component({
  selector: 'app-skater-modal',
  templateUrl: './skater-modal.component.html',
  styleUrls: ['./skater-modal.component.css']
})
export class SkaterModalComponent implements OnInit, OnDestroy {
  skater: null|Skater = null;
  subscription: Subscription;

  constructor(private skaterModalService: SkaterModalService) { }

  ngOnInit() {
    this.subscription = this.skaterModalService.skater
      .subscribe(skater => this.skater = skater);
  }

  ngOnDestroy() {
    // Prevent memory leak when component is destroyed
    this.subscription.unsubscribe();
  }

  onClose() {
    this.skater = null;
  }

}
