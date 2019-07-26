from django.utils.deprecation import MiddlewareMixin

from sites.shortcuts import get_current_site


class CurrentSiteMiddleware(MiddlewareMixin):
    """
    Middleware that sets `site` attribute to request object.
    """

    def process_request(self, request):
        request.site = get_current_site(request)
        if '127.0.0.1' in request.site.domain:
            domain = '127.0.0.1'
        else:
            domain = '.' + request.site.domain

        request.domain = domain
