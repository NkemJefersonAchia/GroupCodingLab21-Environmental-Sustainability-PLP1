#!/usr/bin/python3
from db import DBBase

class RedeemRewards(DBBase):
    def redeem(self, username):
        with self.conn() as conn:
            cur = conn.cursor()
            cur.execute("SELECT points FROM users WHERE username = %s", (username,))
            user = cur.fetchone()
            if not user:
                print("User not found.")
                return
            points = user[0]

            # Fetch unique rewards
            cur.execute("""
                SELECT DISTINCT id, description, cost
                FROM rewards
                ORDER BY id
            """)
            rewards = cur.fetchall()
            if not rewards:
                print("No rewards available.")
                return

            print("Available rewards:")
            for rid, desc, cost in rewards:
                print(f"{rid}. {desc} - Cost: {cost} pts")

            try:
                choice = int(input("Choose reward by ID: ").strip())
            except ValueError:
                print("Invalid input.")
                return

            cur.execute("SELECT cost FROM rewards WHERE id = %s LIMIT 1", (choice,))
            reward = cur.fetchone()
            if not reward:
                print("Invalid reward ID.")
                return
            cost = reward[0]
            if cost > points:
                print("Insufficient points.")
                return

            cur.execute("UPDATE users SET points = points - %s WHERE username = %s", (cost, username))
            conn.commit()
            print(f"Reward redeemed! You spent {cost} points.")