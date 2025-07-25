#!/usr/bin/python3
from db import DBBase

class CollectionPoints(DBBase):
    def list_centers(self):
        with self.conn() as conn:
            cur = conn.cursor()
            # Use DISTINCT so only unique centers are shown
            cur.execute("""
                SELECT DISTINCT name, location, status, distance
                FROM centers
                ORDER BY name
            """)
            rows = cur.fetchall()
        if not rows:
            print("No collection centers found.")
            return
        for name, location, status, distance in rows:
            print(f"{name} - {location} ({status}) - {distance}km away")

    def request_pickup(self, username):
        name = input("Enter collection center name: ").strip()
        weight = input("Enter weight for pickup (kg): ").strip()
        phone = input("Enter your phone number: ").strip()
        print(f"Pickup request sent to {name} for {weight}kg.\nYou will be contacted via {phone} shortly!")
