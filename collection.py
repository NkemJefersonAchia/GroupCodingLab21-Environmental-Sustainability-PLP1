from base import AFRIRecycleBase
class CollectionFinder:
    def find_collection_points(self):
        print("\nWould you like to:")
        print("1. Request a home pickup")
        print("2. Choose from available nearby locations")
        choice = input("Enter your choice: ")

        if choice == "1":
            address = input("Enter your pickup address: ")
            print(f"Pickup request sent for: {address}. A representative will contact you shortly.")

        elif choice == "2":
            locations = [
                "Eco-Friendly Waste Hub - Kicukiro, 10km from your location",
                "Green Cycle Depot - Gasabo, 22km from your location",
                "RecycleSmart Point - Nyarugenge, 7km from your loaction"
            ]

            print("\nSelect from the available locations:")
            for idx, loc in enumerate(locations, 1):
                print(f"{idx}. {loc}")
            
            loc_choice = input("Enter the number of your preferred location: ")

            if loc_choice in ["1", "2", "3"]:
                selected = locations[int(loc_choice) - 1]
                print(f"You have selected: {selected}. You can now drop off your items there.")
            else:
                print("Invalid selection.")

        else:
            print("Invalid selection.")

