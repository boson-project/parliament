# __main__.py

import sys
import signal

from waitress import serve
from . import server


def main():
    """
    Loads a python function, specified by the first command line
    argument, and serves it using the parliament server.
    """
    if (len(sys.argv) != 2):
        print("Usage: python -m", __file__, "<path/to/func.py>")
        exit(1)
    signal.signal(signal.SIGTERM, receive_signal)
    signal.signal(signal.SIGINT, receive_signal)
    app = server.create(server.load(sys.argv[1]))
    serve(app, host='0.0.0.0', port=8080)


def receive_signal(signal_number, frame):
    sys.exit(128 + signal_number)


if __name__ == "__main__":
    main()
