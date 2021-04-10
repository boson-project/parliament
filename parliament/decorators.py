import functools
from cloudevents.http import CloudEvent


def event(_func=None, *,
          event_type="parliament.response",
          event_source="/parliament/function"):
    def event_decorator(func):
        @functools.wraps(func)
        def event_wrapper(*args, **kwargs):
            data = func(*args, **kwargs)
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
