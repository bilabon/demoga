from django.contrib.sites.shortcuts import get_current_site
from django.contrib.sites.models import Site
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        current_site = get_current_site(request)
        # token = self.validate_tid(request)

        # context = self.get_context_data(token.token, **kwargs)
        # context['tid'] = token.pk
        context = {}
        context['site_name'] = current_site.domain
        context['site_host'] = request.get_host()
        # import pdb; pdb.set_trace()
        # current_site.web_site.name
        return self.render_to_response(context)
