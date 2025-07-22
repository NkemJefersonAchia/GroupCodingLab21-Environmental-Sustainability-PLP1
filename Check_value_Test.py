import csv
import os

def estimate_price_and_save_points():
    print("Select the type of recyclable material:")
    print("1. Paper/Cardboard")
    print("2. Plastic")
    print("3. Glass")
    print("4. Metal")
    print("5. Battery")
    
    choice = input("Enter the number corresponding to the material: ")

    rates = {
        "1": ("Paper/Cardboard", 210),
        "2": ("Plastic", 410),
        "3": ("Glass", 40),
        "4": ("Metal", 3380),
        "5": ("Battery", 435)
    }

    if choice in rates:
        material, rate = rates[choice]
        try:
            weight = float(input(f"Enter the weight of {material} in kilograms: "))
            total_value_rwf = rate * weight
            points_earned = (total_value_rwf * 0.25)

            # Read existing points if file exists
            existing_points = 0.0
            if os.path.exists("user_points.csv"):
                with open("user_points.csv", mode="r") as file:
                    reader = csv.DictReader(file)
                    for row in reader:
                        existing_points = float(row["Points"])
                        break  # Read only the first row

            # Add new points
            total_points = existing_points + points_earned

            # Save updated points back to file
            with open("user_points.csv", mode="w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["Points"])
                writer.writerow([total_points])

            print(f"\nYou selected: {material}")
            print(f"Rate: {rate} RWF/kg")
            print(f"Weight: {weight} kg")
            print(f"Estimated Total Value: {total_value_rwf:.2f} RWF")
            print(f"Points Earned This Session: {points_earned:.2f} points")
            print(f"✅ Total Points Saved: {total_points:.2f} points\n")

            return points_earned

        except ValueError:
            print("Invalid weight. Please enter a numeric value.")
            return None
    else:
        print("Invalid choice. Please select a valid material number.")
        return None

def main():
    estimate_price_and_save_points()
if __name__ == "__main__":
    main()
