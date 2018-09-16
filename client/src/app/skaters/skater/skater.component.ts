import { Component, OnInit } from '@angular/core';
import { Router, ActivatedRoute, ParamMap } from '@angular/router';
import { Skater } from '../skater.model';
import { SkaterService } from '../skater.service';


@Component({
  selector: 'app-skater',
  templateUrl: './skater.component.html',
  styleUrls: ['./skater.component.css']
})
export class SkaterComponent implements OnInit {
  skater: Skater | null = null;
  isLoading: boolean;

  constructor(
    private route: ActivatedRoute,
    private router: Router,
    private skaterService: SkaterService
  ) {}

  ngOnInit() {
    this.isLoading = true;
    this.route.paramMap.subscribe((params: ParamMap) => {
      const nhlcom_id = params.get('nhlcom_id');
      this.skaterService.getSkater(nhlcom_id)
        .subscribe(skater => {
          this.skater = skater;
          this.isLoading = false;
        });
    });
  }

}
