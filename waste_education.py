from base import AFRIRecycleBase

class WasteEducation(AFRIRecycleBase):
    def educate(self):
        edu = self.load_data('data/education.csv')
        print("\nWaste Education Tips:")
        for tip in edu:
            print(f"- {tip['tip']}")
