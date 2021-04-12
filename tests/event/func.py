from parliament import Context, event


@event
def main(context: Context):
    """
    Provides a function fixture to be used in tests.
    Also tests that the context acts like both a class and a dict
    """
    assert context.cloud_event is not None
    assert context["cloud_event"] is not None
    assert context.request is not None
    assert context["request"] is not None
    assert len(context) == 2
    for i in context:
        assert i in ["cloud_event", "request"]
    try:
        context["bad_key"]
    except Exception as err:
        assert isinstance(err, KeyError)
    return context.cloud_event.data["message"]
