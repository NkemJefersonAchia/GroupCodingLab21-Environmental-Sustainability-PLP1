def estimate_price_per_kg():
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
            total_value = rate * weight
            print(f"\nYou selected: {material}")
            print(f"Rate: {rate} rwf/kg")
            print(f"Weight: {weight} kg")
            print(f"Estimated Total Value: {total_value:.2f} rwf\n")
            return total_value
        except ValueError:
            print("Invalid weight. Please enter a numeric value.")
            return None
    else:
        print("Invalid choice. Please select a valid material number.")
        return None

def main():
    estimate_price_per_kg()
if __name__ == "__main__":
    main()