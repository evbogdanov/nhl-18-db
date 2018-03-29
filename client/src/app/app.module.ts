import { BrowserModule } from '@angular/platform-browser';
import { ReactiveFormsModule } from '@angular/forms';
import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { HttpClientModule } from '@angular/common/http';

import { AppComponent } from './app.component';
import { HeaderComponent } from './header/header.component';
import { TeamsComponent } from './teams/teams.component';
import { TeamComponent } from './teams/team/team.component';
import { TeamDetailComponent } from './teams/team-detail/team-detail.component';
import { TeamSkaterComponent } from './teams/team-skater/team-skater.component';
import { SkatersComponent } from './skaters/skaters.component';
import { SkaterDetailComponent } from './skaters/skater-detail/skater-detail.component';
import { GoaliesComponent } from './goalies/goalies.component';
import { AboutComponent } from './about/about.component';
import { NotFoundComponent } from './not-found/not-found.component';

import { TeamService } from './teams/team.service';
import { SkaterService } from './skaters/skater.service';
import { SuggestionService } from './suggestions/suggestion.service';

import { ShortPositionPipe } from './players/short-position.pipe';


const appRoutes: Routes = [
  {path: '', redirectTo: '/teams', pathMatch: 'full'},
  {path: 'teams', component: TeamsComponent},
  {path: 'team/:abbrev', component: TeamDetailComponent},
  {path: 'skaters', component: SkatersComponent},
  {path: 'skater/:nhlcom_id', component: SkaterDetailComponent},
  {path: 'goalies', component: GoaliesComponent},
  {path: 'about', component: AboutComponent},
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
    NotFoundComponent,
    SkaterDetailComponent,
    TeamSkaterComponent,
    ShortPositionPipe,
    AboutComponent,
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
