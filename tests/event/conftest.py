import sys
import pytest

from parliament import server


@pytest.fixture
def client():
    """
    Configure a client fixture to be used for integration tests
    """
    func = f"{sys.path[0]}/event"
    app = server.create(server.load(func))
    app.testing = True
    with app.test_client() as client:
        yield client
