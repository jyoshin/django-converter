from django.http import HttpResponse
from django.views.decorators.http import require_http_methods

@require_http_methods(['GET'])
def basic_response(request):
    return HttpResponse('Converter')
