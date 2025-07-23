from db import DBBase

class CollectionPoints(DBBase):
    def list_centers(self):
        with self.conn() as conn:
            cur = conn.cursor()
            cur.execute("SELECT name, location, status, distance FROM centers")
            for row in cur.fetchall():
                print(f"{row[0]} - {row[1]} ({row[2]}) - {row[3]}km away")

    def request_pickup(self, username):
        name = input("Enter collection center name: ")
        weight = input("Enter weight for pickup (kg): ")
        PhoneNumber = input("Enter your phone number: ")
        print(f"Pickup request sent to {name} for {weight}kg. \n You will be contacted via {PhoneNumber} shortly!!")
