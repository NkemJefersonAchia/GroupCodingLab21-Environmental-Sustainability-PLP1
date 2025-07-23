#!/usr/bin/python3
"""Log recyclables and award points."""

from db import DBBase

class LogRecyclables(DBBase):
    PRICES = {'plastic': 10, 'glass': 15, 'paper': 5, 'can': 20}

    def log(self, username):
        t = input("Type (plastic/glass/paper/can): ").strip().lower()
        kg = float(input("Weight (kg): "))
        pts = int(self.PRICES.get(t, 0) * kg)
        with self.conn() as conn:
            cur = conn.cursor()
            cur.execute("""
              INSERT INTO users (username, points)
              VALUES (%s, %s)
              ON DUPLICATE KEY UPDATE points = points + %s
            """, (username, pts, pts))
            conn.commit()
        print(f"You earned {pts} points.")
