from django.http import JsonResponse
from django.views import View
from .models import Team

class TeamsView(View):
    def get(self, request):
        return JsonResponse(
            [t.json for t in Team.objects.all()],
            safe=False
        )
