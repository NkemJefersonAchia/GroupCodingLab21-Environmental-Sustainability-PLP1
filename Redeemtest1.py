import csv

# Define rewards and their costs
REWARDS = {
    "Gift Card ($5)": 50,
    "Coffee Mug": 30,
    "Notebook": 20,
    "Keychain": 10,
    "Pen Set": 15
}

def read_saved_points():
    try:
        with open("user_points.csv", mode="r") as file:
            reader = csv.DictReader(file)
            rows = list(reader)

            if not rows:
                print("Points file is empty.")
                return None

            points = float(rows[0]["Points"])
            print(f"\nYou collected {points:.2f} points.\n")
    except FileNotFoundError:
        print("Points file not found. Please run the logging function first.")
        return None
    except Exception as excep:
        print(f"An error occurred while reading points: {excep}")
        return None

    print("Available Rewards:")
    for i, (reward, cost) in enumerate(REWARDS.items(), start=1):
        print(f"{i}. {reward} - {cost} points")

    try:
        choice = int(input("\nSelect a reward by entering the number (or 0 to skip): "))
        if choice == 0:
            print("No reward selected.")
            return points

        reward_name = list(REWARDS.keys())[choice - 1]
        reward_cost = REWARDS[reward_name]

        if points >= reward_cost:
            points -= reward_cost
            print(f"\nYou have redeemed '{reward_name}' for {reward_cost} points.")
            print(f"Points remaining: {points:.2f}")

            # Update the CSV
            rows[0]["Points"] = f"{points:.2f}"
            with open("user_points.csv", mode="w", newline="") as file:
                writer = csv.DictWriter(file, fieldnames=["Points"])
                writer.writeheader()
                writer.writerows(rows)
        else:
            print(f"\nYou do not have enough points to redeem '{reward_name}'.")
            print(f"Points available: {points:.2f}, needed: {reward_cost}")
    except (ValueError, IndexError):
        print("Invalid selection. Please enter a valid reward number.")

    return points


# File: read_points.py
from Check_value_Test import estimate_price_and_save_points
read_saved_points()
