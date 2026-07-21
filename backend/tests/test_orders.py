def _make_artwork(seeded_client):
    artist_id = seeded_client.get("/artists").get_json()[0]["artist_id"]
    style_id = seeded_client.get("/styles").get_json()[0]["style_id"]
    medium_id = seeded_client.get("/mediums").get_json()[0]["medium_id"]

    artwork = seeded_client.post(
        "/artworks",
        json={
            "title": "Order Test Artwork",
            "artist_id": artist_id,
            "style_id": style_id,
            "medium_id": medium_id,
            "base_price": 4000,
            "status": "Available",
        },
    ).get_json()

    return artwork["artwork_id"]


def _valid_order_payload(artwork_id, **overrides):
    payload = {
        "artwork_id": artwork_id,
        "customer_name": "Rahul Sharma",
        "size": "Large",
        "frame_type": "Wooden",
        "canvas_finish": "Matte",
        "customization": "None",
        "commission_order": 0,
        "gift_wrap": 0,
        "final_price": 4500,
        "order_date": "2026-07-21",
    }
    payload.update(overrides)
    return payload


def test_get_orders_empty(seeded_client):
    resp = seeded_client.get("/orders")
    assert resp.status_code == 200
    assert resp.get_json() == []


def test_create_order(seeded_client):
    artwork_id = _make_artwork(seeded_client)

    resp = seeded_client.post("/orders", json=_valid_order_payload(artwork_id))
    assert resp.status_code == 201
    assert "order_id" in resp.get_json()


def test_create_order_missing_customer_name(seeded_client):
    artwork_id = _make_artwork(seeded_client)

    resp = seeded_client.post(
        "/orders", json=_valid_order_payload(artwork_id, customer_name="")
    )
    assert resp.status_code == 400


def test_create_order_zero_price(seeded_client):
    artwork_id = _make_artwork(seeded_client)

    resp = seeded_client.post(
        "/orders", json=_valid_order_payload(artwork_id, final_price=0)
    )
    assert resp.status_code == 400


def test_create_order_invalid_commission_flag(seeded_client):
    artwork_id = _make_artwork(seeded_client)

    resp = seeded_client.post(
        "/orders", json=_valid_order_payload(artwork_id, commission_order=5)
    )
    assert resp.status_code == 400


def test_create_order_invalid_gift_wrap_flag(seeded_client):
    artwork_id = _make_artwork(seeded_client)

    resp = seeded_client.post(
        "/orders", json=_valid_order_payload(artwork_id, gift_wrap="yes")
    )
    assert resp.status_code == 400


def test_update_order(seeded_client):
    artwork_id = _make_artwork(seeded_client)

    create = seeded_client.post("/orders", json=_valid_order_payload(artwork_id))
    order_id = create.get_json()["order_id"]

    resp = seeded_client.put(
        f"/orders/{order_id}",
        json=_valid_order_payload(artwork_id, customer_name="Updated Name"),
    )
    assert resp.status_code == 200

    check = seeded_client.get("/orders").get_json()
    assert check[0]["customer_name"] == "Updated Name"


def test_delete_order(seeded_client):
    artwork_id = _make_artwork(seeded_client)

    create = seeded_client.post("/orders", json=_valid_order_payload(artwork_id))
    order_id = create.get_json()["order_id"]

    resp = seeded_client.delete(f"/orders/{order_id}")
    assert resp.status_code == 200

    remaining = seeded_client.get("/orders").get_json()
    assert remaining == []


def test_delete_nonexistent_order(seeded_client):
    resp = seeded_client.delete("/orders/9999")
    assert resp.status_code == 404
