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
