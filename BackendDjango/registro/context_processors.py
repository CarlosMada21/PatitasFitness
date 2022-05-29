from django.conf import settings

def globales(request):
    return {'USUARIO': settings.USUARIO}