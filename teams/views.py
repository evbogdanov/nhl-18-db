from django.http import JsonResponse
from django.views import View
from .models import Team

class TeamView(View):
    def get(self, request):
        return JsonResponse({
            'teams': [t.json for t in Team.objects.all()]
        })
