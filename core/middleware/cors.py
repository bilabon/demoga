from django.http import HttpResponse


class CorsMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        if request.is_bot_preview:
            html = '<html><body>A demo preview page for FB.</body></html>'
            response = HttpResponse(html)
            response["Access-Control-Allow-Origin"] = '*'
            return response

        response = self.get_response(request)
        # Code to be executed for each request/response after
        # the view is called.

        if request.origin:
            response = self.get_response(request)
            response["Access-Control-Allow-Origin"] = request.origin
        return response
