# this file is all the database operations this program can perform 
from db import get_connection

# This function run a SQL query that inserts a new player into the database.
def add_player(player_name):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO players (player_name) VALUES (?);",
        (player_name,)
    )
    player_id = cursor.lastrowid
    conn.commit()
    conn.close()
    return player_id
    
# this function gets player id by the name, necessary when adding a new session
def get_player_id_by_name(player_name):
    """
    Look up a player by name.
    Returns the player's ID if found, otherwise None.
    """
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT player_id FROM players WHERE player_name = ?;",
        (player_name,)
    )

    result = cursor.fetchone()
    conn.close()

    if result:
        return result[0]  # player_id
    else:
        return None
    
from db import get_connection

# Allows the user to change a players name. This function doesn't really make lots of sense but I added it do demonstrate my ability to use the update query in this project.
def update_player_name():
    """
    Allows the user to change an existing player's name.
    """
    old_name = input("Enter the current player name you want to edit: ").title()
    new_name = input("Enter the new player name: ").title()

    conn = get_connection()
    cursor = conn.cursor()

    # Check if the player exists
    cursor.execute(
        "SELECT player_id FROM players WHERE player_name = ?;",
        (old_name,)
    )
    result = cursor.fetchone()

    if result is None:
        print(f"No player named {old_name} found.\n")
    else:
        cursor.execute(
            "UPDATE players SET player_name = ? WHERE player_name = ?;",
            (new_name, old_name)
        )
        conn.commit()
        print(f"{old_name} has been renamed to {new_name}.\n")

    conn.close()
    
    
# This functions deletes a player
def delete_player(player_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM players WHERE player_id = ?;",
        (player_id,)
    )

    conn.commit()
    conn.close()

# delete player function, This function allows the user to delete a user based on the player_name
def delete_player_by_name(player_name):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM players WHERE player_name = ?;",
        (player_name,)
    )

    deleted = cursor.rowcount  # how many rows were removed

    conn.commit()
    conn.close()

    return deleted

# This function adds a game session to the game session table using an Insert query
def add_game_session(session_date, difficulty, player_id):
    """
    Add a new game session for the given player.
    Returns the new session_id.
    """
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO game_sessions (player_id, session_date, difficulty)
        VALUES (?, ?, ?);
        """,
        (player_id, session_date, difficulty)
    )

    session_id = cursor.lastrowid
    conn.commit()
    conn.close()

    return session_id

# This function adds a new score into the scores table.
def add_score(player_id, session_id, score):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO scores (player_id, session_id, score) VALUES (?, ?, ?);",
        (player_id, session_id, score)
    )

    conn.commit()
    conn.close()


# This function updates allows the user to update a score, this was added to satisfy the Update data in the CRUD operations requirements in the SQL module.
def update_score():
    """
    Allows the user to update a player's score for a specific session.
    """
    player_name = input("Enter the player's name: ").title()
    conn = get_connection()
    cursor = conn.cursor()

    # Get player_id
    cursor.execute(
        "SELECT player_id FROM players WHERE player_name = ?;",
        (player_name,)
    )
    player = cursor.fetchone()

    if not player:
        print(f"No player named {player_name} found.\n")
        conn.close()
        return

    player_id = player[0]

    # Show all sessions for this player
    cursor.execute(
        """
        SELECT s.session_id, s.session_date, s.difficulty, sc.score
        FROM game_sessions s
        JOIN scores sc ON s.session_id = sc.session_id
        WHERE s.player_id = ?;
        """,
        (player_id,)
    )
    sessions = cursor.fetchall()

    if not sessions:
        print(f"{player_name} has no recorded sessions/scores.\n")
        conn.close()
        return

    print(f"\nSessions for {player_name}:")
    for session_id, date, difficulty, score in sessions:
        print(f"Session ID: {session_id} | Date: {date} | Difficulty: {difficulty} | Score: {score}")

    # Ask which session to update
    session_id_to_update = int(input("Enter the Session ID of the score you want to update: "))
    new_score = int(input("Enter the new score: "))

    cursor.execute(
        "UPDATE scores SET score = ? WHERE session_id = ? AND player_id = ?;",
        (new_score, session_id_to_update, player_id)
    )
    conn.commit()
    print(f"Score for session {session_id_to_update} updated to {new_score}.\n")
    conn.close()


# This function allows the program to delete a user by the user ID.
def delete_player(player_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM players WHERE player_id = ?;",
        (player_id,)
    )

    conn.commit()
    conn.close()


# This function demonstrates a join of data from the db tables. It fetches and returns all the requested data and returns it in the format of a leaderboard.
def get_leaderboard():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT 
            p.player_name,
            MAX(s.score) AS high_score,
            COUNT(s.score) AS games_played
        FROM players p
        JOIN scores s ON p.player_id = s.player_id
        GROUP BY p.player_name
        ORDER BY high_score DESC;
    """)

    results = cursor.fetchall()
    conn.close()
    return results

# Displays the leaderboard to the user
def show_leaderboard():
    print("\n=== GAME LEADERBOARD ===")
    leaderboard = get_leaderboard()
    for player_name, high_score, games_played in leaderboard:
        print(f"{player_name}: High Score = {high_score}, Games Played = {games_played}")
    print()

# Allows user to select date range of scores
def show_scores_by_date():
    start_date = input("Beginning date (YYYY-MM-DD): ")
    end_date = input("End date (YYYY-MM-DD): ")

    print("\n=== SCORES IN DATE RANGE ===")
    results = scores_in_date_range(start_date, end_date)
    for player_name, score, score_date in results:
        print(f"{player_name} | Score: {score} | Date: {score_date}")
    print()

# allows the user to add a new session
def add_new_session():
    new_score = int(input("What is the new score? "))
    new_player = input("What is the player's name? ").title()
    new_date = input("Enter date and time (YYYY-MM-DD HH:MM:SS): ")
    difficulty = input("Difficulty (Easy / Medium / Hard): ").title()

    # Ensure player exists
    player_id = get_player_id_by_name(new_player)
    if player_id is None:
        player_id = add_player(new_player)  # now returns a valid ID

    # Add game session
    session_id = add_game_session(new_date, difficulty, player_id)

    # Add score
    add_score(player_id, session_id, new_score)

    print("New game session added successfully!\n")



# QUERY: Date range filtering. This function shows JOIN's and WHERE to demonstrate effective data filtering. 
def scores_in_date_range(start_date, end_date):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT
            p.player_name,
            s.score,
            gs.session_date
        FROM scores s
        JOIN players p ON s.player_id = p.player_id
        JOIN game_sessions gs ON s.session_id = gs.session_id
        WHERE gs.session_date BETWEEN ? AND ?
        ORDER BY gs.session_date;
        """,
        (start_date, end_date)
    )

    results = cursor.fetchall()
    conn.close()
    return results

