import { Component, OnInit, ViewChild } from '@angular/core';
import { NgForm } from '@angular/forms';

@Component({
  selector: 'app-skaters',
  templateUrl: './skaters.component.html',
  styleUrls: ['./skaters.component.css']
})
export class SkatersComponent implements OnInit {
  @ViewChild('searchForm') searchForm: NgForm;

  // Query matches the backend API
  q = {
    name: '',
    age_from: '',
    age_to: '',
  };

  ngOnInit() {
  }

  onSubmit() {
    for (let field of Object.keys(this.q)) {
      this.q[field] = this.searchForm.value[field];
    }
  }

  onReset() {
    this.searchForm.reset();
  }

}
