from flask import Flask, request, jsonify
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

@app.route("/artists", methods=["POST"])
def add_artist():
    data = request.get_json()

    name = data.get("name")
    specialization = data.get("specialization")
    experience = data.get("experience")
    country = data.get("country")

    if not all([name, specialization, experience, country]):
        return {"error": "All fields are required."}, 400

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO artists (name, specialization, experience, country)
        VALUES (?, ?, ?, ?)
    """, (name, specialization, experience, country))

    conn.commit()
    new_id = cursor.lastrowid
    conn.close()

    return {
        "message": "Artist added successfully.",
        "artist_id": new_id
    }, 201

@app.route("/artists/<int:artist_id>", methods=["PUT"])
def update_artist(artist_id):
    data = request.get_json()

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE artists
        SET name=?, specialization=?, experience=?, country=?
        WHERE artist_id=?
    """, (
        data["name"],
        data["specialization"],
        data["experience"],
        data["country"],
        artist_id
    ))

    conn.commit()
    conn.close()

    return {"message": "Artist updated successfully."}

@app.route("/artists/<int:artist_id>", methods=["DELETE"])
def delete_artist(artist_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM artists WHERE artist_id=?",
        (artist_id,)
    )

    conn.commit()
    conn.close()

    return {"message": "Artist deleted successfully."}

@app.route("/artworks", methods=["GET"])
def get_artworks():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            a.artwork_id,
            a.title,
            ar.name AS artist,
            s.style_name,
            m.medium_name,
            a.base_price,
            a.status
        FROM artworks a
        JOIN artists ar ON a.artist_id = ar.artist_id
        JOIN styles s ON a.style_id = s.style_id
        JOIN mediums m ON a.medium_id = m.medium_id
    """)

    artworks = [dict(row) for row in cursor.fetchall()]

    conn.close()

    return artworks

@app.route("/artworks", methods=["POST"])
def add_artwork():
    data = request.get_json()

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO artworks
        (title, artist_id, style_id, medium_id, base_price, status)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        data["title"],
        data["artist_id"],
        data["style_id"],
        data["medium_id"],
        data["base_price"],
        data["status"]
    ))

    conn.commit()
    artwork_id = cursor.lastrowid
    conn.close()

    return {
        "message": "Artwork added successfully",
        "artwork_id": artwork_id
    }, 201

@app.route("/artworks/<int:artwork_id>", methods=["PUT"])
def update_artwork(artwork_id):
    data = request.get_json()

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE artworks
        SET
            title=?,
            artist_id=?,
            style_id=?,
            medium_id=?,
            base_price=?,
            status=?,
            created_date=?
        WHERE artwork_id=?
    """, (
        data["title"],
        data["artist_id"],
        data["style_id"],
        data["medium_id"],
        data["base_price"],
        data["status"],
        data["created_date"],
        artwork_id
    ))

    conn.commit()
    conn.close()

    return jsonify({"message": "Artwork updated successfully"})

@app.route("/artworks/<int:artwork_id>", methods=["DELETE"])
def delete_artwork(artwork_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM artworks WHERE artwork_id=?",
        (artwork_id,)
    )

    conn.commit()

    if cursor.rowcount == 0:
        conn.close()
        return {"error": "Artwork not found"}, 404

    conn.close()

    return {"message": "Artwork deleted successfully"}

@app.route("/orders", methods=["POST"])
def add_order():
    data = request.get_json()

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO orders
        (
            artwork_id,
            customer_name,
            size,
            frame_type,
            canvas_finish,
            customization,
            commission_order,
            gift_wrap,
            final_price,
            order_date
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        data["artwork_id"],
        data["customer_name"],
        data["size"],
        data["frame_type"],
        data["canvas_finish"],
        data["customization"],
        data["commission_order"],
        data["gift_wrap"],
        data["final_price"],
        data["order_date"]
    ))

    conn.commit()

    order_id = cursor.lastrowid

    conn.close()

    return {
        "message": "Order created successfully",
        "order_id": order_id
    }, 201


if __name__ == "__main__":
    app.run(debug=True)