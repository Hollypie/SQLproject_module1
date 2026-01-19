# this file is all about how my program connects and speaks to my database

import sqlite3

DB_NAME = "leaderboard.db"

def get_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn





