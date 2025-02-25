import json

def test_ping(with_app):
    resp = with_app.test_client().get("/api/v1/ping")
    data = json.loads(resp.data.decode())
    assert resp.status_code == 200
    assert data["message"] == "pong!"

def test_artists(with_app):
    resp = with_app.test_client().get("/api/v1/artists")
    data = json.loads(resp.data.decode())
    assert resp.status_code == 200

def test_create_artist(with_app):
    resp = with_app.test_client().get("/api/v1/artists?artists?name=test")
    print(resp.data)
    data = json.loads(resp.data.decode())
    assert resp.status_code == 200
    assert data["name"] == "test_artist"

def test_create_album(with_app):
    resp = with_app.test_client().get("/api/v1/albums?artist_name=test_artist&name=test_album&release_date=20050201&price=12.34")
    data = json.loads(resp.data.decode())
    assert resp.status_code == 200
    assert data["name"] == "test_album"
    assert data["release_date"] == "20050201"
    assert data["price"] == 12.34
