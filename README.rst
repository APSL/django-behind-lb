=========
Behind_LB
=========

Behind-LB is a very simple and efficient Django middleware to obtain
the client IP address when the project runs behind a trusted load
balancer.

It allows to specify the path that activate the middleware, for example
``/`` or ``/a/specific/path``. The path *must* be specified in the variable
``BEHIND_LB_PATH`` in your settings.py.

It works with any load balancer that sends the public remote address in
a fixed relative position in the header (first, second,... , last).
For example, Amazon ELB puts it in the last position, Google Compute
Load Balancer in the penultimate one. The position *must*
be specified in ``settings.BEHIND_LB_POSITION``.

Quick start
-----------

1. Install the package:

   ``pip install django-behind-lb``

2. Just add ``django-behind-lb`` to your ``INSTALLED_APPS`` setting like this::

    MIDDLEWARE_CLASSES = (
        'behind_lb.middleware.BehindLB',
        ...

3. Configure the path and position in settings.py::

    BEHIND_LB_PATH = "/"
    BEHIND_LB_POSITION = -2 # For Google Compute Engine


4. Try it reading the default ``request.META['REMOTE_ADDR']`` in a View class. It
   should read the real client IP.

Position options
----------------

The ``BEHIND_LB_PATH`` value specifies the position of the real IP address in the
``X-Forwarded-For header``, where 0 is the first (or "left"), 1 the second, -2 the
penultimate position and -1 the last one. Examples::

    BEHIND_LB_POSITION =  0 # First

    BEHIND_LB_POSITION = -2 # Next to last, for Google Compute Engine LB

    BEHIND_LB_POSITION = -1 # Last, for Amazon EC2 LB

In Github
---------

The code is available at https://github.com/APSL/django-behind-lb
