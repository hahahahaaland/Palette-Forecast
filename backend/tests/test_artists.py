def test_get_artists_empty(client):
    resp = client.get("/artists")
    assert resp.status_code == 200
    assert resp.get_json() == []


def test_create_artist(client):
    resp = client.post(
        "/artists",
        json={
            "name": "Aarav Kapoor",
            "specialization": "Abstract",
            "experience": 8,
            "country": "India",
        },
    )
    assert resp.status_code == 201
    body = resp.get_json()
    assert "artist_id" in body


def test_create_artist_missing_name(client):
    resp = client.post(
        "/artists",
        json={"specialization": "Abstract", "experience": 8, "country": "India"},
    )
    assert resp.status_code == 400


def test_create_artist_negative_experience(client):
    resp = client.post(
        "/artists",
        json={
            "name": "Bad Data",
            "specialization": "Abstract",
            "experience": -1,
            "country": "India",
        },
    )
    assert resp.status_code == 400


def test_create_artist_non_numeric_experience(client):
    resp = client.post(
        "/artists",
        json={
            "name": "Bad Data",
            "specialization": "Abstract",
            "experience": "not-a-number",
            "country": "India",
        },
    )
    assert resp.status_code == 400


def test_get_single_artist(client):
    create = client.post(
        "/artists",
        json={
            "name": "Emma Wilson",
            "specialization": "Portrait",
            "experience": 12,
            "country": "United Kingdom",
        },
    )
    artist_id = create.get_json()["artist_id"]

    resp = client.get(f"/artists/{artist_id}")
    assert resp.status_code == 200
    assert resp.get_json()["name"] == "Emma Wilson"


def test_get_nonexistent_artist(client):
    resp = client.get("/artists/9999")
    assert resp.status_code == 404


def test_update_artist(client):
    create = client.post(
        "/artists",
        json={
            "name": "Old Name",
            "specialization": "Realism",
            "experience": 3,
            "country": "USA",
        },
    )
    artist_id = create.get_json()["artist_id"]

    resp = client.put(
        f"/artists/{artist_id}",
        json={
            "name": "New Name",
            "specialization": "Realism",
            "experience": 4,
            "country": "USA",
        },
    )
    assert resp.status_code == 200

    check = client.get(f"/artists/{artist_id}")
    assert check.get_json()["name"] == "New Name"


def test_delete_artist(client):
    create = client.post(
        "/artists",
        json={
            "name": "To Delete",
            "specialization": "Cubism",
            "experience": 2,
            "country": "France",
        },
    )
    artist_id = create.get_json()["artist_id"]

    resp = client.delete(f"/artists/{artist_id}")
    assert resp.status_code == 200

    check = client.get(f"/artists/{artist_id}")
    assert check.status_code == 404


def test_delete_artist_does_not_affect_others(client):
    """Regression-style test: deleting one artist must not remove others."""
    first = client.post(
        "/artists",
        json={
            "name": "Keep Me",
            "specialization": "Landscape",
            "experience": 6,
            "country": "France",
        },
    ).get_json()["artist_id"]

    second = client.post(
        "/artists",
        json={
            "name": "Delete Me",
            "specialization": "Landscape",
            "experience": 6,
            "country": "France",
        },
    ).get_json()["artist_id"]

    client.delete(f"/artists/{second}")

    still_there = client.get(f"/artists/{first}")
    assert still_there.status_code == 200
    assert still_there.get_json()["name"] == "Keep Me"
