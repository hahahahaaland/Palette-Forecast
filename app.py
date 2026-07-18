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

    if not name:
    return {"error": "Artist name is required."}, 400

if not specialization:
    return {"error": "Specialization is required."}, 400

if experience is None:
    return {"error": "Experience is required."}, 400

if experience < 0:
    return {"error": "Experience cannot be negative."}, 400

if not country:
    return {"error": "Country is required."}, 400

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

if not data["title"]:
    return {"error": "Title is required."}, 400

if data["base_price"] <= 0:
    return {"error": "Base price must be greater than zero."}, 400

valid_status = ["Available", "Sold", "Reserved"]

if data["status"] not in valid_status:
    return {
        "error": "Status must be Available, Sold or Reserved."
    }, 400

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

@app.route("/orders", methods=["GET"])
def get_orders():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            order_id,
            artwork_id,
            customer_name,
            size,
            frame_type,
            canvas_finish,
            customization,
            commission_order,
            final_price,
            order_date
        FROM orders
    """)

    orders = [dict(row) for row in cursor.fetchall()]

    conn.close()

    return orders

@app.route("/orders", methods=["POST"])
def add_order():
    data = request.get_json()

    if not data["customer_name"]:
    return {"error": "Customer name is required."}, 400

if data["final_price"] <= 0:
    return {"error": "Final price must be greater than zero."}, 400

if data["commission_order"] not in [0, 1]:
    return {"error": "Commission order must be 0 or 1."}, 400

if data["gift_wrap"] not in [0, 1]:
    return {"error": "Gift wrap must be 0 or 1."}, 400

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

@app.route("/orders/<int:order_id>", methods=["PUT"])
def update_order(order_id):
    data = request.get_json()

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE orders
        SET
            artwork_id=?,
            customer_name=?,
            size=?,
            frame_type=?,
            canvas_finish=?,
            customization=?,
            commission_order=?,
            gift_wrap=?,
            final_price=?,
            order_date=?
        WHERE order_id=?
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
        data["order_date"],
        order_id
    ))

    conn.commit()
    conn.close()

    return {"message": "Order updated successfully"}

@app.route("/orders/<int:order_id>", methods=["DELETE"])
def delete_order(order_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM orders WHERE order_id=?",
        (order_id,)
    )

    conn.commit()

    if cursor.rowcount == 0:
        conn.close()
        return {"error": "Order not found"}, 404

    conn.close()

    return {"message": "Order deleted successfully"}

@app.route("/styles", methods=["GET"])
def get_styles():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM styles")

    styles = [dict(row) for row in cursor.fetchall()]

    conn.close()

    return jsonify(styles)

@app.route("/styles/<int:style_id>", methods=["GET"])
def get_style(style_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM styles WHERE style_id=?",
        (style_id,)
    )

    style = cursor.fetchone()

    conn.close()

    if style:
        return jsonify(dict(style))

    return jsonify({"error": "Style not found"}), 404

@app.route("/styles", methods=["POST"])
def add_style():
    data = request.get_json()

    style_name = data.get("style_name")

    if not style_name or not style_name.strip():
    return {"error": "Style name is required."}, 400

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO styles(style_name) VALUES(?)",
        (style_name,)
    )

    conn.commit()

    style_id = cursor.lastrowid

    conn.close()

    return jsonify({
        "message": "Style added successfully",
        "style_id": style_id
    }), 201

@app.route("/styles/<int:style_id>", methods=["PUT"])
def update_style(style_id):
    data = request.get_json()

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE styles
        SET style_name=?
        WHERE style_id=?
    """, (
        data["style_name"],
        style_id
    ))

    conn.commit()

    if cursor.rowcount == 0:
        conn.close()
        return jsonify({"error": "Style not found"}), 404

    conn.close()

    return jsonify({"message": "Style updated successfully"})

@app.route("/styles/<int:style_id>", methods=["DELETE"])
def delete_style(style_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM styles WHERE style_id=?",
        (style_id,)
    )

    conn.commit()

    if cursor.rowcount == 0:
        conn.close()
        return jsonify({"error": "Style not found"}), 404

    conn.close()

    return jsonify({"message": "Style deleted successfully"})

@app.route("/mediums", methods=["GET"])
def get_mediums():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM mediums")

    mediums = [dict(row) for row in cursor.fetchall()]

    conn.close()

    return jsonify(mediums)

@app.route("/mediums/<int:medium_id>", methods=["GET"])
def get_medium(medium_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM mediums WHERE medium_id=?",
        (medium_id,)
    )

    medium = cursor.fetchone()

    conn.close()

    if medium:
        return jsonify(dict(medium))

    return jsonify({"error": "Medium not found"}), 404

@app.route("/mediums", methods=["POST"])
def add_medium():
    data = request.get_json()

    medium_name = data.get("medium_name")

    if not medium_name or not medium_name.strip():
    return {"error": "Medium name is required."}, 400

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO mediums(medium_name) VALUES(?)",
        (medium_name,)
    )

    conn.commit()

    medium_id = cursor.lastrowid

    conn.close()

    return jsonify({
        "message": "Medium added successfully",
        "medium_id": medium_id
    }), 201

@app.route("/mediums/<int:medium_id>", methods=["PUT"])
def update_medium(medium_id):
    data = request.get_json()

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE mediums
        SET medium_name=?
        WHERE medium_id=?
    """, (
        data["medium_name"],
        medium_id
    ))

    conn.commit()

    if cursor.rowcount == 0:
        conn.close()
        return jsonify({"error": "Medium not found"}), 404

    conn.close()

    return jsonify({"message": "Medium updated successfully"})

@app.route("/mediums/<int:medium_id>", methods=["DELETE"])
def delete_medium(medium_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM mediums WHERE medium_id=?",
        (medium_id,)
    )

    conn.commit()

    if cursor.rowcount == 0:
        conn.close()
        return jsonify({"error": "Medium not found"}), 404

    conn.close()

    return jsonify({"message": "Medium deleted successfully"})



@app.route("/analytics/revenue", methods=["GET"])
def revenue_summary():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            COUNT(*) AS total_orders,
            SUM(final_price) AS total_revenue,
            AVG(final_price) AS average_order_value
        FROM orders
    """)

    summary = dict(cursor.fetchone())

    conn.close()

    return jsonify(summary)

@app.route("/analytics/top-artist", methods=["GET"])
def top_artist():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            ar.name AS artist,
            COUNT(o.order_id) AS total_orders,
            SUM(o.final_price) AS revenue
        FROM orders o
        JOIN artworks aw ON o.artwork_id = aw.artwork_id
        JOIN artists ar ON aw.artist_id = ar.artist_id
        GROUP BY ar.artist_id
        ORDER BY revenue DESC
        LIMIT 1
    """)

    result = cursor.fetchone()

    conn.close()

    if result:
        return jsonify(dict(result))

    return jsonify({"message": "No order data available"})

@app.route("/analytics/top-style", methods=["GET"])
def top_style():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            s.style_name,
            COUNT(o.order_id) AS total_orders,
            SUM(o.final_price) AS revenue
        FROM orders o
        JOIN artworks aw ON o.artwork_id = aw.artwork_id
        JOIN styles s ON aw.style_id = s.style_id
        GROUP BY s.style_id
        ORDER BY total_orders DESC
        LIMIT 1
    """)

    result = cursor.fetchone()

    conn.close()

    if result:
        return jsonify(dict(result))

    return jsonify({"message": "No style data available"})

@app.route("/analytics/top-medium", methods=["GET"])
def top_medium():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            m.medium_name,
            COUNT(o.order_id) AS total_orders,
            SUM(o.final_price) AS revenue
        FROM orders o
        JOIN artworks aw ON o.artwork_id = aw.artwork_id
        JOIN mediums m ON aw.medium_id = m.medium_id
        GROUP BY m.medium_id
        ORDER BY total_orders DESC
        LIMIT 1
    """)

    result = cursor.fetchone()

    conn.close()

    if result:
        return jsonify(dict(result))

    return jsonify({"message": "No medium data available"})

@app.route("/analytics/artwork-status", methods=["GET"])
def artwork_status():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            status,
            COUNT(*) AS total_artworks
        FROM artworks
        GROUP BY status
        ORDER BY total_artworks DESC
    """)

    results = [dict(row) for row in cursor.fetchall()]

    conn.close()

    return jsonify(results)

@app.route("/analytics/gift-wrap", methods=["GET"])
def gift_wrap_statistics():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            gift_wrap,
            COUNT(*) AS total_orders
        FROM orders
        GROUP BY gift_wrap
    """)

    result = [dict(row) for row in cursor.fetchall()]

    conn.close()

    return jsonify(result)

@app.route("/analytics/commissions", methods=["GET"])
def commission_statistics():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            commission_order,
            COUNT(*) AS total_orders
        FROM orders
        GROUP BY commission_order
    """)

    result = [dict(row) for row in cursor.fetchall()]

    conn.close()

    return jsonify(result)

@app.route("/dashboard", methods=["GET"])
def dashboard():
    conn = get_connection()
    cursor = conn.cursor()

    # Artists
    cursor.execute("SELECT COUNT(*) AS total FROM artists")
    total_artists = cursor.fetchone()["total"]

    # Artworks
    cursor.execute("SELECT COUNT(*) AS total FROM artworks")
    total_artworks = cursor.fetchone()["total"]

    # Orders
    cursor.execute("SELECT COUNT(*) AS total FROM orders")
    total_orders = cursor.fetchone()["total"]

    # Revenue
    cursor.execute("SELECT COALESCE(SUM(final_price), 0) AS revenue FROM orders")
    total_revenue = cursor.fetchone()["revenue"]

    # Available artworks
    cursor.execute("""
        SELECT COUNT(*) AS total
        FROM artworks
        WHERE status='Available'
    """)
    available_artworks = cursor.fetchone()["total"]

    # Sold artworks
    cursor.execute("""
        SELECT COUNT(*) AS total
        FROM artworks
        WHERE status='Sold'
    """)
    sold_artworks = cursor.fetchone()["total"]

    conn.close()

    return jsonify({
        "total_artists": total_artists,
        "total_artworks": total_artworks,
        "total_orders": total_orders,
        "total_revenue": total_revenue,
        "available_artworks": available_artworks,
        "sold_artworks": sold_artworks
    })

if __name__ == "__main__":
    app.run(debug=True)