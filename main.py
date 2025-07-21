from log_recyclables import LogRecyclables
from estimate_value import EstimateValue
from redeem_rewards import RedeemRewards
from collection_points import CollectionPoints
from waste_education import WasteEducation

def menu(username):
    while True:
        print("\n--- AFRIRECYCLE MENU ---")
        print("1. Log Recyclables")
        print("2. Check Estimated Value")
        print("3. Redeem Rewards")
        print("4. Find Collection Points")
        print("5. Waste Education")
        print("0. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            LogRecyclables(username).log()
        elif choice == "2":
            EstimateValue(username).show_estimate()
        elif choice == "3":
            RedeemRewards(username).redeem()
        elif choice == "4":
            CollectionPoints(username).find_centers()
        elif choice == "5":
            WasteEducation(username).educate()
        elif choice == "0":
            print("Thank you for recycling!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    user = input("Enter your username: ")
    menu(user)
