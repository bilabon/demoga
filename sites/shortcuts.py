from sites.models import Site


def get_current_site(request):
    return Site.objects.get_current(request)
