#!/usr/bin/python3
"""Populate initial data: centers, tips, rewards."""

from db import DBBase

def populate_initial():
    db = DBBase()
    
    centers = [
        ("EcoCenter", "Bugesera", "open", 2.5),
        ("GreenHub", "Kigali", "closed", 4.0),
        ("AgroPlast Ltd", "Kayonza", "open", 7.8),
        ("RecycleSmart", "Kamonyi", "open", 9.3),
        ("RecycleDepot", "Musanze", "closed", 12.7),
        ("Wastezon", "Huye", "open", 22.3)
    ]
    tips = [
        "Sort plastics from metals.",
        "Clean recyclables before dropping.",
        "Avoid hazardous waste in recycling bins.",
        "Reuse before recycling."
    ]
    rewards = [
        ("Airtime (500rwf)", 250),
        ("Gift card (4000rwf)", 5000),
        ("Chapati (10pcs)", 50),
        ("Milk", 75)
    ]

    with db.conn() as conn:
        cur = conn.cursor()
        cur.executemany(
            "INSERT IGNORE INTO centers (name, location, status, distance) "
            "VALUES (%s, %s, %s, %s)",
            centers
        )
        cur.executemany(
            "INSERT IGNORE INTO tips (tip) VALUES (%s)",
            [(t,) for t in tips]
        )
        cur.executemany(
            "INSERT IGNORE INTO rewards (description, cost) VALUES (%s, %s)",
            rewards
        )
        conn.commit()

if __name__ == "__main__":
    populate_initial()
    print("Initial data populated.")
