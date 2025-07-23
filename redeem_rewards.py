from db import DBBase

class RedeemRewards(DBBase):
    def redeem(self, username):
        with self.conn() as conn:
            cur = conn.cursor()
            cur.execute("SELECT points FROM users WHERE username = %s", (username,))
            user = cur.fetchone()
            if not user:
                print("User not found."); return
            points = user[0]

            cur.execute("SELECT id, description, cost FROM rewards")
            rewards = cur.fetchall()
            for r in rewards:
                print(f"{r[0]}. {r[1]} - Cost: {r[2]} pts")

            choice = int(input("Choose reward by ID: "))
            cur.execute("SELECT cost FROM rewards WHERE id = %s", (choice,))
            reward = cur.fetchone()
            if not reward or reward[0] > points:
                print("Invalid choice or insufficient points.")
                return

            cur.execute("UPDATE users SET points = points - %s WHERE username = %s", (reward[0], username))
            conn.commit()
            print("Reward redeemed!")
