
from types import FunctionType
from parliament import server
from flask import Flask
from cloudevents.http import CloudEvent, to_binary


def test_load():
  """
  Test that we can load a python function
  """
  func = server.load("./func.py")
  assert isinstance(func.main, FunctionType)


def test_create():
  """
  Test tha we can create a Flask app with the function
  """
  app = server.create(server.load("./func.py"))
  assert isinstance(app, Flask)


def test_readiness_endpoint(client):
  """
  Test /health/readiness
  """
  rv = client.get("/health/readiness")
  assert b"OK" in rv.data


def test_liveness_endpoint(client):
  """
  Test /health/liveness
  """
  rv = client.get("/health/liveness")
  assert b"OK" in rv.data


def test_post_cloud_event(client):
  """
  Test that we can successfully receive a CloudEvent
  """
  attributes = {
    "type": "com.test.parliament",
    "source": "https://test.com/parliament",
  }
  data = {"message": "Hello World!"}
  event = CloudEvent(attributes, data)
  headers, body = to_binary(event)

  rv = client.post("/", data=body, headers=headers)
  assert rv.data == b"Hello World!"


def test_post_data(client):
  """
  Test that we can handle simple HTTP POST
  """
  data = '{"message": "Hi, Friend!"}'
  rv = client.post(
    "/",
    data=data,
    headers={"Content-Type": "application/json"})
  assert rv.data == b"Hi, Friend!"
