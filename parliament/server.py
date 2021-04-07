import os
import sys

from flask import Flask, request
from cloudevents.http import from_http


def load(path):
  func_dir = os.path.realpath(path)
  sys.path.append(func_dir)
  import func
  return func


def create(func):
  app = Flask(__name__)

  @app.route("/", methods=["POST"])
  def handle_post():
    context = {
      'request': request
    }
    try:
      context['cloud_event'] = from_http(request.headers, request.get_data())
    except Exception:
      app.logger.warning('No CloudEvent available')

    try:
      print(request.json)
      return func.main(context)
    except Exception as err:
      return f"Function threw {err}", 500

  @app.route("/", methods=["GET"])
  def handle_get():
    context = {
      'request': request
    }
    return func.main(context)

  @app.route("/health/liveness")
  def liveness():
    return "OK"

  @app.route("/health/readiness")
  def readiness():
    return "OK"

  return app
