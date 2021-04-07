import sys
import pytest

from parliament import server


@pytest.fixture
def client():
  func = f"{sys.path[0]}/func.py"
  app = server.create(server.load(func))
  with app.test_client() as client:
    yield client
