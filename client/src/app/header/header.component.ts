import { Component, Input } from '@angular/core';
import { Renderer2 } from '@angular/core';
import { Router } from '@angular/router';

import { Suggestion } from '../suggestions/suggestion.model';
import { SuggestionService } from '../suggestions/suggestion.service';


@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.css']
})
export class HeaderComponent {
  @Input() shadow: any;
  showLoadingIndicator: boolean = false;
  noSuggestions: boolean = false;
  suggestions: Suggestion[] = [];

  constructor(
    private renderer: Renderer2,
    private router: Router,
    private suggestionService: SuggestionService
  ) { }

  getSuggestions(name) {
    if (name === '') {
      this.noSuggestions = false;
      this.suggestions = [];
    }
    else {
      this.showLoadingIndicator = true;
      this.suggestionService.getSuggestions(name)
        .subscribe(suggestions => {
          this.showLoadingIndicator = false;
          this.noSuggestions = suggestions.length === 0;
          this.suggestions = suggestions;
        })
    }
  }

  clearSuggestionsAndNavigate(input, destination) {
    input.value = '';
    this.suggestions = [];
    this.router.navigate(destination);
  }

  activateSearching(nav, inp) {
    this.renderer.addClass(nav, 'searching');
    this.renderer.addClass(this.shadow, 'main-shadow_activated');
    this.renderer.selectRootElement(inp).focus();
  }

  deactivateSearching(nav) {
    this.renderer.removeClass(nav, 'searching');
    this.renderer.removeClass(this.shadow, 'main-shadow_activated');
    this.showLoadingIndicator = false;
    this.noSuggestions = false;
    this.suggestions = [];
  }

}
