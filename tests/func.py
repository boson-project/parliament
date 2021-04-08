from parliament.server import Context


def main(context: Context):
    """
    Provides a function fixture to be used in tests
    """
    if context.cloud_event is not None:
        event = context.cloud_event
        return event.data["message"], 200
    else:
        data = context.request.get_json(silent=True)
        print(data)
        return data["message"]
