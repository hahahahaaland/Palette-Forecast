def _ids(seeded_client):
    """Grab the ids of the seeded artist/style/medium so we can create
    a valid artwork against them."""
    artist_id = seeded_client.get("/artists").get_json()[0]["artist_id"]
    style_id = seeded_client.get("/styles").get_json()[0]["style_id"]
    medium_id = seeded_client.get("/mediums").get_json()[0]["medium_id"]
    return artist_id, style_id, medium_id


def test_get_artworks_empty(seeded_client):
    resp = seeded_client.get("/artworks")
    assert resp.status_code == 200
    assert resp.get_json() == []


def test_create_artwork(seeded_client):
    artist_id, style_id, medium_id = _ids(seeded_client)

    resp = seeded_client.post(
        "/artworks",
        json={
            "title": "Sunset Over Hills",
            "artist_id": artist_id,
            "style_id": style_id,
            "medium_id": medium_id,
            "base_price": 5000,
            "status": "Available",
        },
    )
    assert resp.status_code == 201
    assert "artwork_id" in resp.get_json()


def test_create_artwork_invalid_status(seeded_client):
    artist_id, style_id, medium_id = _ids(seeded_client)

    resp = seeded_client.post(
        "/artworks",
        json={
            "title": "Bad Status Art",
            "artist_id": artist_id,
            "style_id": style_id,
            "medium_id": medium_id,
            "base_price": 5000,
            "status": "NotARealStatus",
        },
    )
    assert resp.status_code == 400


def test_create_artwork_zero_price(seeded_client):
    artist_id, style_id, medium_id = _ids(seeded_client)

    resp = seeded_client.post(
        "/artworks",
        json={
            "title": "Free Art",
            "artist_id": artist_id,
            "style_id": style_id,
            "medium_id": medium_id,
            "base_price": 0,
            "status": "Available",
        },
    )
    assert resp.status_code == 400


def test_update_artwork(seeded_client):
    artist_id, style_id, medium_id = _ids(seeded_client)

    create = seeded_client.post(
        "/artworks",
        json={
            "title": "Original Title",
            "artist_id": artist_id,
            "style_id": style_id,
            "medium_id": medium_id,
            "base_price": 3000,
            "status": "Available",
        },
    )
    artwork_id = create.get_json()["artwork_id"]

    resp = seeded_client.put(
        f"/artworks/{artwork_id}",
        json={
            "title": "Updated Title",
            "artist_id": artist_id,
            "style_id": style_id,
            "medium_id": medium_id,
            "base_price": 3500,
            "status": "Reserved",
        },
    )
    assert resp.status_code == 200

    check = seeded_client.get("/artworks").get_json()
    assert check[0]["title"] == "Updated Title"
    assert check[0]["status"] == "Reserved"


def test_delete_artwork(seeded_client):
    artist_id, style_id, medium_id = _ids(seeded_client)

    create = seeded_client.post(
        "/artworks",
        json={
            "title": "To Delete",
            "artist_id": artist_id,
            "style_id": style_id,
            "medium_id": medium_id,
            "base_price": 1000,
            "status": "Available",
        },
    )
    artwork_id = create.get_json()["artwork_id"]

    resp = seeded_client.delete(f"/artworks/{artwork_id}")
    assert resp.status_code == 200

    remaining = seeded_client.get("/artworks").get_json()
    assert remaining == []


def test_delete_nonexistent_artwork(seeded_client):
    resp = seeded_client.delete("/artworks/9999")
    assert resp.status_code == 404
