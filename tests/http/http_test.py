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


def test_get(client):
    """
    Test that we can handle simple HTTP GET
    """
    rv = client.get("/")
    assert rv.data == b"Howdy!"


def test_handles_exceptions(client):
    """
    Test that a raised exception will be handled correctly
    """
    data = '{"message": "throw"}'
    rv = client.post(
        "/",
        data=data,
        headers={"Content-Type": "application/json"})
    assert rv.data == b"Function raised Whoops!"
    assert rv.status_code == 500
