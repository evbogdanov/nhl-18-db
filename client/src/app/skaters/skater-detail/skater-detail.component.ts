import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { Skater } from '../skater.model';
import { SkaterService } from '../skater.service';


@Component({
  selector: 'app-skater-detail',
  templateUrl: './skater-detail.component.html',
  styleUrls: ['./skater-detail.component.css']
})
export class SkaterDetailComponent implements OnInit {
  skater: Skater | null = null;

  constructor(private route: ActivatedRoute,
              private skaterService: SkaterService) {}

  ngOnInit() {
    const nhlcom_id = this.route.snapshot.paramMap.get('nhlcom_id');
    this.skaterService.getSkater(nhlcom_id)
      .subscribe(skater => this.skater = skater);
  }

}
