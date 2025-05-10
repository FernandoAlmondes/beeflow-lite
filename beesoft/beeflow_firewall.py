from django.http import HttpResponseForbidden
from django.conf import settings

class IPsPermitidos:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        allowed_ips = getattr(settings, "IPS_PERMITIDOS", [])
        
        # Verifica se X-Forwarded-For existe
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0].strip()  # pega o primeiro IP (do cliente)
        else:
            ip = request.META.get('REMOTE_ADDR')

        if ip not in allowed_ips:
            return HttpResponseForbidden("Acesso negado!")

        response = self.get_response(request)
        return response
