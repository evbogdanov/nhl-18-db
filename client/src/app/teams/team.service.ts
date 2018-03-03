import { Injectable } from '@angular/core';
import { Team } from './team.model';

const MOCK_TEAMS: Team[] = [
  {
    "abbrev": "ana",
    "name": "Anaheim Ducks",
    "country": {
      "abbrev": "usa",
      "name": "USA"
    },
    "division": "Pacific",
    "conference": "Western",
    "is_active": true,
    "img": "/static/img/team/ana.svg"
  },
  {
    "abbrev": "ari",
    "name": "Arizona Coyotes",
    "country": {
      "abbrev": "usa",
      "name": "USA"
    },
    "division": "Pacific",
    "conference": "Western",
    "is_active": true,
    "img": "/static/img/team/ari.svg"
  },
  {
    "abbrev": "bos",
    "name": "Boston Bruins",
    "country": {
      "abbrev": "usa",
      "name": "USA"
    },
    "division": "Atlantic",
    "conference": "Eastern",
    "is_active": true,
    "img": "/static/img/team/bos.svg"
  },
  {
    "abbrev": "buf",
    "name": "Buffalo Sabres",
    "country": {
      "abbrev": "usa",
      "name": "USA"
    },
    "division": "Atlantic",
    "conference": "Eastern",
    "is_active": true,
    "img": "/static/img/team/buf.svg"
  },
  {
    "abbrev": "car",
    "name": "Carolina Hurricanes",
    "country": {
      "abbrev": "usa",
      "name": "USA"
    },
    "division": "Metropolitan",
    "conference": "Eastern",
    "is_active": true,
    "img": "/static/img/team/car.svg"
  },
  {
    "abbrev": "cbj",
    "name": "Columbus Blue Jackets",
    "country": {
      "abbrev": "usa",
      "name": "USA"
    },
    "division": "Metropolitan",
    "conference": "Eastern",
    "is_active": true,
    "img": "/static/img/team/cbj.svg"
  },
  {
    "abbrev": "cgy",
    "name": "Calgary Flames",
    "country": {
      "abbrev": "can",
      "name": "Canada"
    },
    "division": "Pacific",
    "conference": "Western",
    "is_active": true,
    "img": "/static/img/team/cgy.svg"
  },
  {
    "abbrev": "chi",
    "name": "Chicago Blackhawks",
    "country": {
      "abbrev": "usa",
      "name": "USA"
    },
    "division": "Central",
    "conference": "Western",
    "is_active": true,
    "img": "/static/img/team/chi.svg"
  },
  {
    "abbrev": "col",
    "name": "Colorado Avalanche",
    "country": {
      "abbrev": "usa",
      "name": "USA"
    },
    "division": "Central",
    "conference": "Western",
    "is_active": true,
    "img": "/static/img/team/col.svg"
  },
  {
    "abbrev": "dal",
    "name": "Dallas Stars",
    "country": {
      "abbrev": "usa",
      "name": "USA"
    },
    "division": "Central",
    "conference": "Western",
    "is_active": true,
    "img": "/static/img/team/dal.svg"
  },
  {
    "abbrev": "det",
    "name": "Detroit Red Wings",
    "country": {
      "abbrev": "usa",
      "name": "USA"
    },
    "division": "Atlantic",
    "conference": "Eastern",
    "is_active": true,
    "img": "/static/img/team/det.svg"
  },
  {
    "abbrev": "edm",
    "name": "Edmonton Oilers",
    "country": {
      "abbrev": "can",
      "name": "Canada"
    },
    "division": "Pacific",
    "conference": "Western",
    "is_active": true,
    "img": "/static/img/team/edm.svg"
  },
  {
    "abbrev": "fla",
    "name": "Florida Panthers",
    "country": {
      "abbrev": "usa",
      "name": "USA"
    },
    "division": "Atlantic",
    "conference": "Eastern",
    "is_active": true,
    "img": "/static/img/team/fla.svg"
  },
  {
    "abbrev": "lak",
    "name": "Los Angeles Kings",
    "country": {
      "abbrev": "usa",
      "name": "USA"
    },
    "division": "Pacific",
    "conference": "Western",
    "is_active": true,
    "img": "/static/img/team/lak.svg"
  },
  {
    "abbrev": "min",
    "name": "Minnesota Wild",
    "country": {
      "abbrev": "usa",
      "name": "USA"
    },
    "division": "Central",
    "conference": "Western",
    "is_active": true,
    "img": "/static/img/team/min.svg"
  },
  {
    "abbrev": "mtl",
    "name": "Montreal Canadiens",
    "country": {
      "abbrev": "can",
      "name": "Canada"
    },
    "division": "Atlantic",
    "conference": "Eastern",
    "is_active": true,
    "img": "/static/img/team/mtl.svg"
  },
  {
    "abbrev": "njd",
    "name": "New Jersey Devils",
    "country": {
      "abbrev": "usa",
      "name": "USA"
    },
    "division": "Metropolitan",
    "conference": "Eastern",
    "is_active": true,
    "img": "/static/img/team/njd.svg"
  },
  {
    "abbrev": "nsh",
    "name": "Nashville Predators",
    "country": {
      "abbrev": "usa",
      "name": "USA"
    },
    "division": "Central",
    "conference": "Western",
    "is_active": true,
    "img": "/static/img/team/nsh.svg"
  },
  {
    "abbrev": "nyi",
    "name": "New York Islanders",
    "country": {
      "abbrev": "usa",
      "name": "USA"
    },
    "division": "Metropolitan",
    "conference": "Eastern",
    "is_active": true,
    "img": "/static/img/team/nyi.svg"
  },
  {
    "abbrev": "nyr",
    "name": "New York Rangers",
    "country": {
      "abbrev": "usa",
      "name": "USA"
    },
    "division": "Metropolitan",
    "conference": "Eastern",
    "is_active": true,
    "img": "/static/img/team/nyr.svg"
  },
  {
    "abbrev": "ott",
    "name": "Ottawa Senators",
    "country": {
      "abbrev": "can",
      "name": "Canada"
    },
    "division": "Atlantic",
    "conference": "Eastern",
    "is_active": true,
    "img": "/static/img/team/ott.svg"
  },
  {
    "abbrev": "phi",
    "name": "Philadelphia Flyers",
    "country": {
      "abbrev": "usa",
      "name": "USA"
    },
    "division": "Metropolitan",
    "conference": "Eastern",
    "is_active": true,
    "img": "/static/img/team/phi.svg"
  },
  {
    "abbrev": "pit",
    "name": "Pittsburgh Penguins",
    "country": {
      "abbrev": "usa",
      "name": "USA"
    },
    "division": "Metropolitan",
    "conference": "Eastern",
    "is_active": true,
    "img": "/static/img/team/pit.svg"
  },
  {
    "abbrev": "sjs",
    "name": "San Jose Sharks",
    "country": {
      "abbrev": "usa",
      "name": "USA"
    },
    "division": "Pacific",
    "conference": "Western",
    "is_active": true,
    "img": "/static/img/team/sjs.svg"
  },
  {
    "abbrev": "stl",
    "name": "St. Louis Blues",
    "country": {
      "abbrev": "usa",
      "name": "USA"
    },
    "division": "Central",
    "conference": "Western",
    "is_active": true,
    "img": "/static/img/team/stl.svg"
  },
  {
    "abbrev": "tbl",
    "name": "Tampa Bay Lightning",
    "country": {
      "abbrev": "usa",
      "name": "USA"
    },
    "division": "Atlantic",
    "conference": "Eastern",
    "is_active": true,
    "img": "/static/img/team/tbl.svg"
  },
  {
    "abbrev": "tor",
    "name": "Toronto Maple Leafs",
    "country": {
      "abbrev": "can",
      "name": "Canada"
    },
    "division": "Atlantic",
    "conference": "Eastern",
    "is_active": true,
    "img": "/static/img/team/tor.svg"
  },
  {
    "abbrev": "van",
    "name": "Vancouver Canucks",
    "country": {
      "abbrev": "can",
      "name": "Canada"
    },
    "division": "Pacific",
    "conference": "Western",
    "is_active": true,
    "img": "/static/img/team/van.svg"
  },
  {
    "abbrev": "vgk",
    "name": "Vegas Golden Knights",
    "country": {
      "abbrev": "usa",
      "name": "USA"
    },
    "division": "Pacific",
    "conference": "Western",
    "is_active": true,
    "img": "/static/img/team/vgk.svg"
  },
  {
    "abbrev": "wpg",
    "name": "Winnipeg Jets",
    "country": {
      "abbrev": "can",
      "name": "Canada"
    },
    "division": "Central",
    "conference": "Western",
    "is_active": true,
    "img": "/static/img/team/wpg.svg"
  },
  {
    "abbrev": "wsh",
    "name": "Washington Capitals",
    "country": {
      "abbrev": "usa",
      "name": "USA"
    },
    "division": "Metropolitan",
    "conference": "Eastern",
    "is_active": true,
    "img": "/static/img/team/wsh.svg"
  },
  {
    "abbrev": "phx",
    "name": "Phoenix Coyotes",
    "country": {
      "abbrev": "usa",
      "name": "USA"
    },
    "division": "Pacific",
    "conference": "Western",
    "is_active": false,
    "img": "/static/img/team/phx.svg"
  },
  {
    "abbrev": "atl",
    "name": "Atlanta Thrashers",
    "country": {
      "abbrev": "usa",
      "name": "USA"
    },
    "division": "Southeast",
    "conference": "Western",
    "is_active": false,
    "img": "/static/img/team/atl.svg"
  }
];

@Injectable()
export class TeamService {
  getTeams(): Team[] {
    // TODO: fetch teams from the server
    return MOCK_TEAMS;
  }
}
 
