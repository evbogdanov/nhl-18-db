import { Injectable } from '@angular/core';
import { BehaviorSubject } from 'rxjs/BehaviorSubject';
import { Skater } from './skater.model';


@Injectable()
export class SkaterModalService {
  private skaterSource = new BehaviorSubject<Skater|null>(null);

  skater = this.skaterSource.asObservable();

  constructor() { }

  changeSkater(skater: null|Skater) {
    this.skaterSource.next(skater);
  }

}
