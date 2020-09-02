from .models import Link


def ctx_social(request):
    ctx_dict = {}
    links = Link.objects.all()
    for link in links:
        ctx_dict[link.key] = link.url
    return ctx_dict
