class CorsMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)

        # origin = request.META.get("HTTP_ORIGIN")
        response["Access-Control-Allow-Origin"] = request.domain

        # if not origin and response.site:
        #     response["Access-Control-Allow-Origin"] = "*"
        # elif origin and response.site:
        #     response["Access-Control-Allow-Origin"] = origin

        # # Code to be executed for each request/response after
        # # the view is called.

        # import pdb
        # pdb.set_trace()

        # from django.http import Http404
        # raise Http404

        return response
