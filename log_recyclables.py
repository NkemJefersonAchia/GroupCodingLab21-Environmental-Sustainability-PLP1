#!/usr/bin/python3
"""Log recyclables and show RWF rate (not total cash value)."""

from db import DBBase

class LogRecyclables(DBBase):
    # RWF per kilogram for each type
    RATES = {
        'plastic': 410,
        'glass':   40,
        'paper':   210,
        'can':     435
    }

    def log(self, username):
        t = input("Type (plastic/glass/paper/can): ").strip().lower()
        rate = self.RATES.get(t)
        if rate is None:
            print("Unknown type:", t)
            return

        try:
            kg = float(input("Weight (kg): ").strip())
        except ValueError:
            print("Invalid weight.")
            return

        pts = int(rate * kg * 0.25)  # points = 25% of total RWF

        with self.conn() as conn:
            cur = conn.cursor()
            cur.execute("""
              INSERT INTO users (username, points)
              VALUES (%s, %s)
              ON DUPLICATE KEY UPDATE points = points + %s
            """, (username, pts, pts))
            conn.commit()

        print(f"Rate: {rate} RWF/kg")
        print(f"Points earned: {pts}")