#!/usr/bin/python3
"""Display waste education tips."""

from db import DBBase

class WasteEducation(DBBase):
    def educate(self):
        with self.conn() as conn:
            cur = conn.cursor()
            cur.execute("SELECT tip FROM tips")
            rows = cur.fetchall()
        print("\nWaste Education Tips:")
        for (tip,) in rows:
            print("- " + tip)
