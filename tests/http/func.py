from parliament import Context


def main(context: Context):
    """
    Provides a function fixture to be used in tests
    """
    data = context.request.get_json(silent=True)
    if data is None or "message" not in data:
        return "Howdy!"
    if data["message"] == "throw":
        raise NameError("Whoops!")
    return data["message"]
