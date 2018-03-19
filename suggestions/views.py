from django.http import JsonResponse
from django.views import View
from .models import get_suggestions

class SuggestionsView(View):
    def get(self, request):
        name = request.GET.get('name', '')
        suggestions = get_suggestions(name)
        return JsonResponse(suggestions)
