from django.conf import settings
from django.utils.deprecation import MiddlewareMixin


class DisableCSRFOnDebug(MiddlewareMixin):

    def process_request(self, req):
        if settings.DEBUG:
            attr = '_dont_enforce_csrf_checks'
            if not getattr(req, attr, False):
                setattr(req, attr, True)
