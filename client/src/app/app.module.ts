import { BrowserModule } from '@angular/platform-browser';
import { ReactiveFormsModule } from '@angular/forms';
import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { HttpClientModule } from '@angular/common/http';

import { AppComponent } from './app.component';
import { HeaderComponent } from './header/header.component';
import { HomeComponent } from './home/home.component'
import { TeamsComponent } from './teams/teams.component';
import { SkatersComponent } from './skaters/skaters.component';
import { GoaliesComponent } from './goalies/goalies.component';
import { TeamComponent } from './teams/team/team.component';
import { TeamDetailComponent } from './teams/team-detail/team-detail.component';
import { NotFoundComponent } from './not-found/not-found.component';

import { TeamService } from './teams/team.service';
import { SkaterService } from './skaters/skater.service';
import { SuggestionService } from './suggestions/suggestion.service';


const appRoutes: Routes = [
  {path: '', component: HomeComponent},
  {path: 'teams', component: TeamsComponent},
  {path: 'team/:abbrev', component: TeamDetailComponent},
  {path: 'skaters', component: SkatersComponent},
  {path: 'goalies', component: GoaliesComponent},
  {path: '**', component: NotFoundComponent},
];

@NgModule({
  declarations: [
    AppComponent,
    HeaderComponent,
    TeamsComponent,
    SkatersComponent,
    GoaliesComponent,
    TeamComponent,
    TeamDetailComponent,
    HomeComponent,
    NotFoundComponent,
  ],
  imports: [
    BrowserModule,
    ReactiveFormsModule,
    HttpClientModule,
    RouterModule.forRoot(appRoutes),
  ],
  providers: [
    TeamService,
    SkaterService,
    SuggestionService,
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
