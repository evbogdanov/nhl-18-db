import { Component, AfterViewInit, Input, ViewChild } from '@angular/core';
import { Renderer2 } from '@angular/core';
import { Router, NavigationEnd } from '@angular/router';

import { Suggestion } from '../suggestions/suggestion.model';
import { SuggestionService } from '../suggestions/suggestion.service';


@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.css']
})
export class HeaderComponent implements AfterViewInit {
  @Input() shadow: any;
  showLoadingIndicator: boolean = false;
  noSuggestions: boolean = false;
  suggestions: Suggestion[] = [];

  @ViewChild('indicatorLair') indicatorLair;
  @ViewChild('indicator') indicator;
  @ViewChild('navItemAbout') navItemAbout;
  @ViewChild('navItemGoalies') navItemGoalies;
  @ViewChild('navItemSkaters') navItemSkaters;
  @ViewChild('navItemTeams') navItemTeams;

  constructor(
    private renderer: Renderer2,
    private router: Router,
    private suggestionService: SuggestionService
  ) { }

  ngAfterViewInit() {
    this.router.events.subscribe((event) => {
      if (event instanceof NavigationEnd) {
        this.moveIndicator(event.url);
      }
    });
  }

  moveIndicator(nextUrl) {
    // Fix default URL
    if (nextUrl === '/') {
      nextUrl = '/teams';
    }

    // Space between 2 nav items
    const styles = window.getComputedStyle(this.indicatorLair.nativeElement);
    const marginLeft = parseInt(styles.marginLeft, 10);
    const space = marginLeft * 2;

    // Indicator moves from right to left
    const urls = [{url: '/about', item: this.navItemAbout},
                  {url: '/goalies', item: this.navItemGoalies},
                  {url: '/skaters', item: this.navItemSkaters},
                  {url: '/teams', item: this.navItemTeams}];

    let [navItem, width, distance, notFound] = [null, null, 0, true];
    for (const u of urls) {
      navItem = u.item;
      width = navItem.nativeElement.clientWidth;
      distance += space + width
      if (u.url === nextUrl) {
        notFound = false;
        break;
      }
    }

    // Header doesn't contain a link for nextUrl. So move to the initial
    // position.
    if (notFound) {
      [width, distance] = [0, 0];
    }

    this.renderer.setStyle(this.indicator.nativeElement, 'left', `-${distance}px`);
    this.renderer.setStyle(this.indicator.nativeElement, 'width', `${width}px`);
  }

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

  deactivateSearching(nav, inp) {
    inp.value = '';
    this.renderer.removeClass(nav, 'searching');
    this.renderer.removeClass(this.shadow, 'main-shadow_activated');
    this.showLoadingIndicator = false;
    this.noSuggestions = false;
    this.suggestions = [];
  }

}
