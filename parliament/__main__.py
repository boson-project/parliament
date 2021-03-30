# __main__.py

import sys, os

from flask import Flask, request
from cloudevents.http import from_http
from waitress import serve
import signal

def main():
  def receive_signal(signal_number, frame):
    sys.exit(128 + signal_number)
    return

  signal.signal(signal.SIGTERM, receive_signal)
  signal.signal(signal.SIGINT, receive_signal)

  load_function()
  import func

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
    return func.main(context)

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

  serve(app, host='0.0.0.0', port=8080)


def load_function():
  if (len(sys.argv) != 2):
    print("Usage: python -m", __file__, "<path/to/func.py>")
    exit(1)
  func_dir = os.path.realpath(sys.argv[1])
  sys.path.append(func_dir)

if __name__ == "__main__":
  main()
