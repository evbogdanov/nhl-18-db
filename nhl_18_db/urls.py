from django.urls import path, re_path
from django.contrib import admin
from django.views.generic import TemplateView
from countries.views import CountriesView
from teams.views import TeamsView, TeamView
from players.views import SkatersView
from suggestions.views import SuggestionsView


urlpatterns = [
    ## Admin
    path('admin/', admin.site.urls),

    ## API
    path('api/countries/', CountriesView.as_view()),
    path('api/teams/', TeamsView.as_view()),
    path('api/teams/<abbrev>/', TeamView.as_view()),
    path('api/skaters/', SkatersView.as_view()),
    path('api/suggestions/', SuggestionsView.as_view()),

    ## Angular
    re_path(r'^', TemplateView.as_view(template_name='index.html')),
]
