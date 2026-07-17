from flask import Flask, request
from db import get_connection

app = Flask(__name__)


@app.route("/")
def home():
    return {
        "project": "Palette Forecast",
        "message": "Welcome to the Palette Forecast API!"
    }


@app.route("/artists", methods=["GET"])
def get_artists():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM artists")

    artists = [dict(row) for row in cursor.fetchall()]

    conn.close()

    return artists


@app.route("/artists/<int:artist_id>", methods=["GET"])
def get_artist(artist_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM artists WHERE artist_id=?",
        (artist_id,)
    )

    artist = cursor.fetchone()

    conn.close()

    if artist:
        return dict(artist)

    return {"error": "Artist not found"}, 404


if __name__ == "__main__":
    app.run(debug=True)