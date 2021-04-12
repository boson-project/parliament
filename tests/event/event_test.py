from cloudevents.http import CloudEvent, to_binary


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
    assert rv.data == b'"Hello World!"'
    assert rv.headers["ce-source"] == "/parliament/function"
    assert rv.headers["ce-type"] == "parliament.response"
