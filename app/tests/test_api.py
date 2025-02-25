import json

def test_ping(with_app):
    resp = with_app.test_client().get("/api/v1/ping")
    data = json.loads(resp.data.decode())
    assert resp.status_code == 200
    assert data["message"] == "pong!"