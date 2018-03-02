import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';


import { AppComponent } from './app.component';
import { HeaderComponent } from './header/header.component';
import { TeamsComponent } from './teams/teams.component';
import { SkatersComponent } from './skaters/skaters.component';
import { GoaliesComponent } from './goalies/goalies.component';
import { TeamComponent } from './teams/team/team.component';


@NgModule({
  declarations: [
    AppComponent,
    HeaderComponent,
    TeamsComponent,
    SkatersComponent,
    GoaliesComponent,
    TeamComponent
  ],
  imports: [
    BrowserModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
