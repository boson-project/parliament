import sys
import pytest

from parliament import server


@pytest.fixture
def client():
    """
    Configure a client fixture to be used for integraton tests
    """
    func = f"{sys.path[0]}/func.py"
    app = server.create(server.load(func))
    with app.test_client() as client:
        yield client
