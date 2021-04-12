import sys
from types import FunctionType
from flask import Flask
from parliament import server


def test_load():
    """
    Test that we can load a python function
    """
    func = server.load(f"{sys.path[0]}/http")
    assert isinstance(func.main, FunctionType)


def test_create():
    """
    Test that we can create a Flask app with the function
    """
    app = server.create(server.load(f"{sys.path[0]}/http"))
    assert isinstance(app, Flask)
