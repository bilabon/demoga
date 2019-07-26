from django.utils.html import escape
from django.conf import settings


class CookieMixin:
    site_type_id = 1

    def fetch_by_key(self, request, key, from_cookie, default):
        if from_cookie:
            value = request.COOKIES.get(key, default=default)
        else:
            value = (request.GET.get(key, default=default) or
                     request.POST.get(key, default=default))
        return value

    def fetch_ref_id(self, request, from_cookie=False):

        if self.site_type_id == 3:
            # if WL - return web_sites.ref_id
            return int(self.site_ref_id) if self.site_ref_id else 0

        if from_cookie:
            rid = 0
        else:
            rid = self.fetch_by_key(request, 'rid', from_cookie, default=0)  # new
        ref_id = self.fetch_by_key(request, 'ref_id', from_cookie, default=0)  # old
        try:
            rid = int(rid)
        except ValueError:
            rid = 0
        try:
            ref_id = int(ref_id)
        except ValueError:
            ref_id = 0

        ref_id = rid if rid else ref_id
        if from_cookie:
            ref_id = ref_id or 0
        else:
            ref_id = ref_id if ref_id else settings.DEFAULT_REF_ID
        return int(ref_id)

    def fetch_sub_id(self, request, from_cookie=False):
        if from_cookie:
            sid = ''
        else:
            sid = self.fetch_by_key(request, 'sid', from_cookie, default='')  # new

        sub_id = self.fetch_by_key(request, 'sub_id', from_cookie, default='')  # old
        sub_id = sid if sid else sub_id
        sub_id = escape(sub_id)[:20]
        return sub_id

    def fetch_dsc(self, request, from_cookie=False):
        dsc = self.fetch_by_key(request, 'dsc', from_cookie, default='')
        dsc = escape(dsc)[:20]
        return dsc


class CookieMiddleware(CookieMixin):
    EXPIRES_DAYS = 172800  # 2 days

    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)

        # # Code to be executed for each request/response after
        # # the view is called.

        dsc = self.fetch_dsc(request, from_cookie=False)
        if dsc:
            response.set_cookie('dsc', dsc, max_age=self.EXPIRES_DAYS,
                                domain=request.cookie_domain)

        rid = self.fetch_ref_id(request, from_cookie=False)
        if rid:
            response.set_cookie('rid', rid, max_age=self.EXPIRES_DAYS,
                                domain=request.cookie_domain)

        sid = self.fetch_sub_id(request, from_cookie=False)
        if sid:
            response.set_cookie('sid', sid, max_age=self.EXPIRES_DAYS,
                                domain=request.cookie_domain)
        return response
