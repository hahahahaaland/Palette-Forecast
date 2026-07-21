def test_get_styles_empty(client):
    resp = client.get("/styles")
    assert resp.status_code == 200
    assert resp.get_json() == []


def test_create_style(client):
    resp = client.post("/styles", json={"style_name": "Abstract"})
    assert resp.status_code == 201
    assert "style_id" in resp.get_json()


def test_create_style_blank_name(client):
    resp = client.post("/styles", json={"style_name": "   "})
    assert resp.status_code == 400


def test_get_single_style_not_found(client):
    resp = client.get("/styles/9999")
    assert resp.status_code == 404


def test_update_style(client):
    create = client.post("/styles", json={"style_name": "Old Style"})
    style_id = create.get_json()["style_id"]

    resp = client.put(f"/styles/{style_id}", json={"style_name": "New Style"})
    assert resp.status_code == 200

    check = client.get(f"/styles/{style_id}")
    assert check.get_json()["style_name"] == "New Style"


def test_delete_style(client):
    create = client.post("/styles", json={"style_name": "Temporary Style"})
    style_id = create.get_json()["style_id"]

    resp = client.delete(f"/styles/{style_id}")
    assert resp.status_code == 200

    check = client.get(f"/styles/{style_id}")
    assert check.status_code == 404


def test_delete_nonexistent_style(client):
    resp = client.delete("/styles/9999")
    assert resp.status_code == 404


def test_get_mediums_empty(client):
    resp = client.get("/mediums")
    assert resp.status_code == 200
    assert resp.get_json() == []


def test_create_medium(client):
    resp = client.post("/mediums", json={"medium_name": "Oil Paint"})
    assert resp.status_code == 201
    assert "medium_id" in resp.get_json()


def test_create_medium_blank_name(client):
    resp = client.post("/mediums", json={"medium_name": ""})
    assert resp.status_code == 400


def test_update_medium(client):
    create = client.post("/mediums", json={"medium_name": "Old Medium"})
    medium_id = create.get_json()["medium_id"]

    resp = client.put(f"/mediums/{medium_id}", json={"medium_name": "New Medium"})
    assert resp.status_code == 200

    check = client.get(f"/mediums/{medium_id}")
    assert check.get_json()["medium_name"] == "New Medium"


def test_delete_medium(client):
    create = client.post("/mediums", json={"medium_name": "Temporary Medium"})
    medium_id = create.get_json()["medium_id"]

    resp = client.delete(f"/mediums/{medium_id}")
    assert resp.status_code == 200

    check = client.get(f"/mediums/{medium_id}")
    assert check.status_code == 404


def test_delete_nonexistent_medium(client):
    resp = client.delete("/mediums/9999")
    assert resp.status_code == 404
