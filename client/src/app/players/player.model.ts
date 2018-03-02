import { Country } from '../countries/country.model';
import { Team } from '../teams/team.model';

export interface Player {
  readonly nhlcom_id: number;
  readonly country: Country;
  readonly team: Team;

  readonly first_name: string;
  readonly last_name: string;
  readonly born: string;
  readonly age: number;
  readonly number: number;

  readonly salary: number;
  readonly years_left: number;

  readonly height: number;
  readonly weight: number;

  readonly draft_team: Team | null;
  readonly draft_year: number | null;
  readonly draft_round: number | null;
  readonly draft_overall: number | null;

  readonly potential: string;
  readonly overall: number;

  readonly img: string;
}
