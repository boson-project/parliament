import os
import sys
import traceback

from flask import Flask, request
from cloudevents.http import CloudEvent, from_http, to_binary
from .invocation import Context


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
        return invoke(func, context)

    @app.route("/", methods=["GET"])
    def handle_get():
        context = Context(request)
        return invoke(func, context)

    @app.route("/health/liveness")
    def liveness():
        return "OK"

    @app.route("/health/readiness")
    def readiness():
        return "OK"

    return app


def invoke(func, context):
    try:
        resp = func.main(context)
        if isinstance(resp, CloudEvent):
            headers, body = to_binary(resp)
            return body, headers
        else:
            return resp
    except Exception as err:
        traceback.print_exc()
        print("caught", err)
        return f"Function raised {err}", 500
