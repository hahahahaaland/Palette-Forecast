from db import get_connection


def create_tables():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS artists (
        artist_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        specialization TEXT,
        experience INTEGER,
        country TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS styles (
        style_id INTEGER PRIMARY KEY AUTOINCREMENT,
        style_name TEXT NOT NULL UNIQUE
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS mediums (
        medium_id INTEGER PRIMARY KEY AUTOINCREMENT,
        medium_name TEXT NOT NULL UNIQUE
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS artworks (
        artwork_id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        artist_id INTEGER,
        style_id INTEGER,
        medium_id INTEGER,
        base_price REAL,
        status TEXT,
        created_date TEXT,

        FOREIGN KEY (artist_id) REFERENCES artists(artist_id),
        FOREIGN KEY (style_id) REFERENCES styles(style_id),
        FOREIGN KEY (medium_id) REFERENCES mediums(medium_id)
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS orders (
        order_id INTEGER PRIMARY KEY AUTOINCREMENT,
        artwork_id INTEGER,
        customer_name TEXT,
        size TEXT,
        frame_type TEXT,
        canvas_finish TEXT,
        customization TEXT,
        commission_order INTEGER,
        final_price REAL,
        order_date TEXT,

        FOREIGN KEY (artwork_id) REFERENCES artworks(artwork_id)
    )
    """)

    conn.commit()
    conn.close()

    print("Database schema created successfully!")


if __name__ == "__main__":
    create_tables()