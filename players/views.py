from django.http import JsonResponse
from django.views import View
from .models import Skater


class SkatersView(View):
    def get(self, request):
        return JsonResponse(Skater.search(request.GET),
                            safe=False)


class SkaterView(View):
    def get(self, request, nhlcom_id):
        try:
            skater = Skater.objects.get(nhlcom_id=nhlcom_id)
            return JsonResponse(skater.json)
        except Skater.DoesNotExist:
            return JsonResponse(None, safe=False)
