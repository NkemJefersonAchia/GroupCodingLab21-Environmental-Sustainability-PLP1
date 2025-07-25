#!/usr/bin/python3
"""Display two random waste education tips."""

from db import DBBase

class WasteEducation(DBBase):
    def educate(self):
        with self.conn() as conn:
            cur = conn.cursor()
            # Select 2 random tips from the tips table
            cur.execute("SELECT tip FROM tips ORDER BY RAND() LIMIT 2")
            rows = cur.fetchall()

        print("\nWaste Education Tips:")
        for (tip,) in rows:
            print("- " + tip)
