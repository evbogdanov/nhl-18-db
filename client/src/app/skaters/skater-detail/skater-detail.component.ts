import { Component, OnInit } from '@angular/core';
import { Router, ActivatedRoute, ParamMap } from '@angular/router';
import { Skater } from '../skater.model';
import { SkaterService } from '../skater.service';


@Component({
  selector: 'app-skater-detail',
  templateUrl: './skater-detail.component.html',
  styleUrls: ['./skater-detail.component.css']
})
export class SkaterDetailComponent implements OnInit {
  skater: Skater | null = null;

  constructor(
    private route: ActivatedRoute,
    private router: Router,
    private skaterService: SkaterService
  ) {}

  ngOnInit() { 
    this.route.paramMap.subscribe((params: ParamMap) => {
      const nhlcom_id = params.get('nhlcom_id');
      this.skaterService.getSkater(nhlcom_id)
        .subscribe(skater => this.skater = skater);
    });
  }

}
