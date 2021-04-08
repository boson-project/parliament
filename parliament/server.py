import os
import sys

from flask import Flask, request, Request
from cloudevents.http import from_http, CloudEvent


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


def load(path):
    """
    Load a python file with a main() function and return the module
    """
    func_dir = os.path.realpath(path)
    sys.path.append(func_dir)
    import func
    return func


def create(func):
    """
    Create a Flask app with kube health endpoints, exposing 'func' at /
    """
    app = Flask(__name__)

    @app.route("/", methods=["POST"])
    def handle_post():
        context = Context(request)
        try:
            context.cloud_event = from_http(request.headers,
                                            request.get_data())
        except Exception:
            app.logger.warning('No CloudEvent available')

        try:
            return func.main(context)
        except Exception as err:
            return f"Function threw {err}", 500

    @app.route("/", methods=["GET"])
    def handle_get():
        context = Context(request)
        return func.main(context)

    @app.route("/health/liveness")
    def liveness():
        return "OK"

    @app.route("/health/readiness")
    def readiness():
        return "OK"

    return app
