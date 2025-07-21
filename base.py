class AFRIRecycleBase:
    def __init__(self, username):
        self.username = username

    def load_data(self, filepath):
        import csv
        with open(filepath, 'r', newline='') as file:
            return list(csv.DictReader(file))

    def save_data(self, filepath, fieldnames, rows):
        import csv
        with open(filepath, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)
