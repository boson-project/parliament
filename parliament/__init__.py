# __init__.py


from flask import Request
from cloudevents.http import CloudEvent


class Context(object):
    """
    Class holding invocation context.

    ...

    Attributes
    ----------
    request:
        Flask HTTP request
    cloud_event:
        CloudEvent if any
    """
    request: Request
    cloud_event: CloudEvent
    __slots__ = ['request', 'cloud_event']

    def __init__(self, req: Request):
        self.request = req
        self.cloud_event = None


__version__ = "0.0.5"
__all__ = ["server", "Context"]
