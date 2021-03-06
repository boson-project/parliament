from parliament import event
from cloudevents.http import CloudEvent


def test_returns_cloud_event():
    """
    Test that a function decorated with @event returns a cloud_event
    """
    @event
    def f():
        return "data"
    assert isinstance(f(), CloudEvent)


def test_defaults():
    """
    Test the default values for the @event decorator
    """
    @event
    def f():
        return "data"

    ce = f()
    assert ce["type"] == "parliament.response"
    assert ce["source"] == "/parliament/function"
    assert ce.data == "data"


def test_accepts_source():
    """
    Test that the @event decorator accepts a 'source' parameter
    """
    @event(event_source="/parliament/test")
    def f():
        return "data"
    ce = f()
    assert ce["type"] == "parliament.response"
    assert ce["source"] == "/parliament/test"
    assert ce.data == "data"


def test_accepts_type():
    """
    Test that the @event decorator accepts a 'type' parameter
    """
    @event(event_type="parliament.test")
    def f():
        return "data"
    ce = f()
    assert ce["type"] == "parliament.test"
    assert ce["source"] == "/parliament/function"
    assert ce.data == "data"


def test_event_data():
    """
    Test that the @event decorator includes the value
    returned from invocation as the event data
    """
    @event
    def f(data: str) -> str:
        return data
    ce = f("test value")
    assert ce.data == "test value"


def test_handles_returned_events():
    """
    Test that the @event decorator can detect when a function
    has returned a CloudEvent, and simply pass it on.
    """
    @event
    def f() -> CloudEvent:
        attributes = {
          "type": "user.type",
          "source": "/user/source"
        }
        return CloudEvent(attributes, "Hola!")
    ce = f()
    assert ce.data == "Hola!"
    assert ce["type"] == "user.type"
    assert ce["source"] == "/user/source"
