from urllib.parse import urlparse
from django.utils.deprecation import MiddlewareMixin

from sites.shortcuts import get_current_site


class CurrentSiteMiddleware(MiddlewareMixin):
    """
    Middleware that sets `site` attribute to request object.
    """

    def process_request(self, request):
        request.site = get_current_site(request)

        if '127.0.0.1' in request.site.domain:
            request.cookie_domain = '127.0.0.1'
        else:
            request.cookie_domain = '.' + request.site.domain

        request.is_bot_preview = False
        request.origin = None
        origin = request.META.get('HTTP_ORIGIN', '')
        if origin:
            if urlparse(origin).hostname.endswith(request.site.domain):
                request.origin = origin
            else:
                request.is_bot_preview = True
