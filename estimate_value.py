#!/usr/bin/python3
"""Show user’s total points and cash equivalent."""

from db import DBBase

class EstimateValue(DBBase):
    def show(self, username):
        with self.conn() as conn:
            cur = conn.cursor()
            cur.execute("SELECT points FROM users WHERE username = %s", (username,))
            row = cur.fetchone()
        if row:
            print(f"{username}: {row[0]} points (~{row[0]} RWF)")
        else:
            print("No record for user.")
