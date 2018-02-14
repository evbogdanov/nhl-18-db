from django.urls import path
from django.contrib import admin
from countries.views import CountryView
from teams.views import TeamView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('countries/', CountryView.as_view()),
    path('teams/', TeamView.as_view()),
]
