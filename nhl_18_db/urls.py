from django.urls import path
from django.contrib import admin
from countries.views import CountryView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('countries/', CountryView.as_view()),
]
