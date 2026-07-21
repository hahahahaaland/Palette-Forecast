"""
Shared pytest fixtures for the backend test suite.

IMPORTANT SAFETY NOTE:
Every test that uses the `client` fixture below runs against a brand-new,
throwaway SQLite file created fresh for that single test (via pytest's
built-in `tmp_path` fixture). It is NEVER the real
`database/palette_forecast.db`.

This is done by monkeypatching `db.DB_PATH` before the Flask app is used,
so calls to `get_connection()` open the temp file instead of your real
database. When the test finishes, pytest deletes the temp directory
automatically.

Practical effect: even a test that calls a DELETE endpoint, or a test that
crashes halfway through, cannot touch your real artists/artworks/orders
data. There is no code path in these tests that ever opens the real
database file.
"""

import os
import sys

import pytest

# Make sure `backend/` is importable regardless of where pytest is run from
BACKEND_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if BACKEND_DIR not in sys.path:
    sys.path.insert(0, BACKEND_DIR)

import db  # noqa: E402
import models  # noqa: E402


@pytest.fixture
def client(tmp_path, monkeypatch):
    """Flask test client backed by an isolated temp SQLite database."""
    temp_db_path = tmp_path / "test_palette_forecast.db"

    # Redirect every get_connection() call to the temp file for this test only
    monkeypatch.setattr(db, "DB_PATH", str(temp_db_path))

    # Build a fresh schema in the temp DB (does not touch the real DB)
    models.create_tables()

    # Import app AFTER the monkeypatch is in place
    from app import app as flask_app

    flask_app.config["TESTING"] = True

    with flask_app.test_client() as test_client:
        yield test_client


@pytest.fixture
def seeded_client(client):
    """A client fixture with one artist, one style, and one medium already
    inserted, since artworks/orders require valid foreign keys."""
    client.post(
        "/artists",
        json={
            "name": "Test Artist",
            "specialization": "Abstract",
            "experience": 5,
            "country": "Testland",
        },
    )
    client.post("/styles", json={"style_name": "Test Style"})
    client.post("/mediums", json={"medium_name": "Test Medium"})
    return client
