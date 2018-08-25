# nhl-18-db

NHL 18 Database

## Development

Create `./shell` script:
```
#!/usr/bin/env bash

export DATABASE_URL="..."
export SECRET_KEY="..."

pipenv shell
```

Then:
```
$ ./shell
$ ./manage.py runserver
```


## Tests
```
$ ./manage.py test players
```


## Deployment to Heroku

Go to the Heroku Dashboard and configure variables:
- DATABASE_URL
- SECRET_KEY

```
$ git push heroku master
$ heroku run python manage.py migrate
```


## Create everything
```
$ heroku run python manage.py createcountries
$ heroku run python manage.py createteams
$ heroku run python manage.py createskaters
$ heroku run python manage.py setteamratings
$ heroku run python manage.py makeskatersform
```


## Delete everything
```
$ heroku run python manage.py deletecountries
```


## Front end

Development:
```
$ ng build --watch true
$ ./manage.py synctemplate
```

Production:
```
$ ng build --target=production
$ ./manage.py synctemplate
```
