import { Component, OnInit } from '@angular/core';
import { Suggestion } from '../suggestions/suggestion.model';
import { SuggestionService } from '../suggestions/suggestion.service';


@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {
  suggestions: Suggestion[] = [];

  constructor(private suggestionService: SuggestionService) { }

  ngOnInit() {
  }

  getSuggestions(name) {
    if (name === '') {
      this.suggestions = [];
    }
    else {
      this.suggestionService.getSuggestions(name)
        .subscribe(suggestions => this.suggestions = suggestions)
    }
  }
}
