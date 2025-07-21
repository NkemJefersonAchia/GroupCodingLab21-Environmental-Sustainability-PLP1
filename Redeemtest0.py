import csv

def read_saved_points():
    try:
        with open("user_points.csv", mode="r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                points = float(row["Points"])
                print(f"You have {points:.2f} points saved.")
                return points
    except FileNotFoundError:
        print("Points file not found. Please run the logging function first.")
        return None
    except Exception as excep:
        print(f"An error occurred while reading points: {excep}")
        return None

# File: read_points.py
from Tests import estimate_price_and_save_points  # optional if you want to reuse
read_saved_points()