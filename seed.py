from db import get_connection 

def seed_data():
    conn = get_connection()
    cursor = conn.cursor()

    # Clear existing data so seeding is repeatable
    cursor.execute("DELETE FROM scores;")
    cursor.execute("DELETE FROM game_sessions;")
    cursor.execute("DELETE FROM players;")

    # ---- Seed Players ----
    players = [
        ("Alice",),
        ("Bob",),
        ("Charlie",),
        ("Dana",)
    ]

    cursor.executemany(
        "INSERT INTO players (player_name) VALUES (?);",
        players
    )

    # Fetch player IDs
    cursor.execute("SELECT player_id, player_name FROM players;")
    player_ids = {name: pid for pid, name in cursor.fetchall()}

    # ---- Seed Game Sessions ----
    game_sessions = [
        (player_ids["Alice"], "2025-11-05 10:00:00", "Easy"),
        (player_ids["Alice"], "2025-06-06 14:30:00", "Hard"),
        (player_ids["Bob"], "2025-10-06 16:00:00", "Medium"),
        (player_ids["Charlie"], "2026-01-07 18:15:00", "Easy"),
        (player_ids["Dana"], "2026-01-07 19:45:00", "Hard")
    ]

    cursor.executemany(
        """
        INSERT INTO game_sessions (player_id, session_date, difficulty)
        VALUES (?, ?, ?);
        """,
        game_sessions
    )

    # Fetch session IDs
    cursor.execute("SELECT session_id, player_id FROM game_sessions;")
    sessions = cursor.fetchall()

    # ---- Seed Scores ----
    scores = [
        (sessions[0][0], sessions[0][1], 1500),
        (sessions[1][0], sessions[1][1], 2200),
        (sessions[2][0], sessions[2][1], 1800),
        (sessions[3][0], sessions[3][1], 1300),
        (sessions[4][0], sessions[4][1], 2600)
    ]

    cursor.executemany(
        """
        INSERT INTO scores (session_id, player_id, score)
        VALUES (?, ?, ?);
        """,
        scores
    )

    conn.commit()
    conn.close()
