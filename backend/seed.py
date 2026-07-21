from db import get_connection


def seed_data():
    conn = get_connection()
    cursor = conn.cursor()

    # Styles
    styles = [
        ("Abstract",),
        ("Minimalism",),
        ("Realism",),
        ("Impressionism",),
        ("Monochrome",),
        ("Pop Art",),
        ("Cubism",),
        ("Surrealism",),
        ("Contemporary",),
        ("Landscape",),
        ("Portrait",),
    ]

    cursor.executemany(
        """
        INSERT OR IGNORE INTO styles(style_name)
        VALUES (?)
    """,
        styles,
    )

    # Mediums
    mediums = [
        ("Oil Paint",),
        ("Acrylic",),
        ("Watercolor",),
        ("Oil Pastels",),
        ("Colored Pencil",),
        ("Graphite",),
        ("Gouache",),
        ("Charcoal",),
        ("Ink",),
        ("Digital",),
    ]

    cursor.executemany(
        """
        INSERT OR IGNORE INTO mediums(medium_name)
        VALUES (?)
    """,
        mediums,
    )

    # Artists
    artists = [
        ("Aarav Kapoor", "Abstract", 8, "India"),
        ("Emma Wilson", "Portrait", 12, "United Kingdom"),
        ("Noah Kim", "Watercolor", 5, "South Korea"),
        ("Sofia Rossi", "Impressionism", 10, "Italy"),
        ("Lucas Martin", "Landscape", 7, "France"),
        ("Mia Chen", "Pop Art", 6, "Singapore"),
        ("Kabir Mehta", "Minimalism", 9, "India"),
        ("Olivia Brown", "Contemporary", 11, "Canada"),
        ("Ethan Walker", "Graphite", 4, "Australia"),
        ("Yuki Tanaka", "Surrealism", 13, "Japan"),
    ]

    cursor.executemany(
        """
        INSERT INTO artists
        (name, specialization, experience, country)
        VALUES (?, ?, ?, ?)
    """,
        artists,
    )

    conn.commit()
    conn.close()

    print("Seed data inserted successfully!")


if __name__ == "__main__":
    seed_data()
