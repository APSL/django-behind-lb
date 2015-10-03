from django.core.exceptions import MiddlewareNotUsed
from django.conf import settings
import re

class BehindLB(object):
    """ Middleware that get the real IP from de x-forwarded-for
        Don't use it if you are not sure your load balancer return the real ip


    BEHIND_LB_PATH = False

        0 == first
        1 == second
        ...
        -2 == second from the right ## For Google Compute Engine LB
        -1 == last                  ## For Amazon EC2 LB
    BEHIND_LB_POSITION = None
    """

    """ HTTP headers to look for the IPs
        from https://github.com/un33k/django-ipware/blob/master/ipware/defaults.py
    """
    BEHIND_LB_PRECEDENCE = (
            'HTTP_X_FORWARDED_FOR',
            'HTTP_FORWARDED_FOR',
            'HTTP_FORWARDED',
    )

    def __init__(self):
        try:
            if isinstance(settings.BEHIND_LB_PATH, str) and isinstance(settings.BEHIND_LB_POSITION, int):
                self.position = settings.BEHIND_LB_POSITION
                self.base_path = settings.BEHIND_LB_PATH
                self.len = len(self.base_path)
                self.seps = re.compile(r'[, ]') # To split by ',' and ' '
                return
        except NameError:
            pass

        raise MiddlewareNotUsed("BehindLB disabled, check BEHIND_LB_PATH and BEHIND_LB_POSITION in settings.py")


    def process_request(self, request):
        """ Process ingress requests """

        """ Check if the request's path is under the base path """
        if self.base_path not in request.path_info[:self.len]:
            return

        """ Loop over the different header names in BEHIND_LB_PRECEDENCE """
        for key in self.BEHIND_LB_PRECEDENCE:
            try:
                """ Split the header string, by ',' and ' ' """
                ips = [ip for ip in re.split(self.seps, request.META[key]) if len(ip)]
                request.META['REMOTE_ADDR'] = ips[self.position]
            except (KeyError, IndexError):
                pass
        return
