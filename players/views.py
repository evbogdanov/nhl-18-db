from django.http import JsonResponse
from django.views import View
from .models import Skater

class SkatersView(View):
    def get(self, request):
        return JsonResponse(Skater.search(request.GET),
                            safe=False)
