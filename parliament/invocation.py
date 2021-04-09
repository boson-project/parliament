from collections.abc import Mapping
from typing import Optional

from flask import Request
from cloudevents.http import CloudEvent


class Context(Mapping):
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
    cloud_event: Optional[CloudEvent]
    __slots__ = ['request', 'cloud_event']

    def __init__(self, req: Request):
        self.request = req
        self.cloud_event = None

    # for backward compatibility reason this class can behave like a Mapping

    def __getitem__(self, item):
        if item == 'request' and self.request is not None:
            return self.request
        if item == 'cloud_event' and self.cloud_event is not None:
            return self.cloud_event
        raise KeyError(item)

    def __iter__(self):
        if self.request is not None:
            yield 'request'
        if self.cloud_event is not None:
            yield 'cloud_event'

    def __len__(self):
        return int(self.request is not None) +\
               int(self.cloud_event is not None)
