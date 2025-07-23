#!/usr/bin/python3
"""AFRIRECYCLE CLI: initialize DB and run feature menu."""

from init_data import populate_initial 
from log_recyclables import LogRecyclables
from estimate_value import EstimateValue
from redeem_rewards import RedeemRewards
from collection_points import CollectionPoints
from waste_education import WasteEducation

def menu(username):
    lr = LogRecyclables()
    ev = EstimateValue()
    rr = RedeemRewards()
    cp = CollectionPoints()
    we = WasteEducation()

    while True:
        print("""
--- AFRIRECYCLE MENU ---
1. Log Recyclables Collected
2. Check Estimated Cash Value
3. Convert Points into Rewards
4. Locate Collection Points
5. Request Home Pickup
6. Waste Education
0. Exit
""")
        choice = input("Select option: ").strip()
        if choice == "1":
            lr.log(username)
        elif choice == "2":
            ev.show(username)
        elif choice == "3":
            rr.redeem(username)
        elif choice == "4":
            cp.list_centers()
        elif choice == "5":
            cp.request_pickup(username)
        elif choice == "6":
            we.educate()
        elif choice == "0":
            print("Thank you for recycling—goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    populate_initial()  # Creates tables and loads data: centers, rewards, tips
    user = input("Enter your username: ").strip()
    menu(user)
