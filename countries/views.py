from django.http import JsonResponse
from django.views import View
from .models import Country

class CountryView(View):
    def get(self, request):
        return JsonResponse({
            'countries': list(Country.objects.all().values())
        })
