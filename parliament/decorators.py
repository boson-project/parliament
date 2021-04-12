import functools
from cloudevents.http import CloudEvent


def event(_func=None, *,
          event_type="parliament.response",
          event_source="/parliament/function"):
    """
    Provides an @event decorator that accomplishes a few of things.

    1. It converts a function's response value into the data for a CloudEvent
       sending the event back as the response to the caller.

    2. It allows a function developer to specify the CloudEvent
       source and type attributes:

           @event(event_source="/my/source", event_type="my.type")

    3. Defaults the event source and type attributes to "/parliament/function"
       and "parliament.response", respectively.
    """
    def event_decorator(func):
        @functools.wraps(func)
        def event_wrapper(*args, **kwargs):
            data = func(*args, **kwargs)
            if isinstance(data, CloudEvent):
                return data
            attributes = {
              "type": event_type,
              "source": event_source
            }
            return CloudEvent(attributes, data)
        return event_wrapper

    if _func is None:
        return event_decorator
    else:
        return event_decorator(_func)
