from django.urls import path
from django.contrib import admin
from countries.views import CountriesView
from teams.views import TeamsView
from players.views import SkatersView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('countries/', CountriesView.as_view()),
    path('teams/', TeamsView.as_view()),
    path('skaters/', SkatersView.as_view()),
]
