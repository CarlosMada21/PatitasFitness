from django.conf import settings

def global_usuario(request):
    return {'USUARIO': settings.USUARIO}

def global_login(request):
    return {'LOGIN': settings.LOGIN}