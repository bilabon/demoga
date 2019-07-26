from sites.shortcuts import get_current_site
from sites.models import Site
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        current_site = get_current_site(request)
        context = {}
        context['site_name'] = current_site.domain
        context['site_host'] = request.get_host()
        return self.render_to_response(context)
