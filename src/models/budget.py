from kivy.lang import Builder
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
import os

# Load the .kv file
kv_dir = os.path.dirname(__file__)
Builder.load_file(os.path.join(kv_dir, '../view/budget.kv'))


class BudgetScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def save_allocation(self):
        income = self.ids.income_input.text
        budget = self.ids.budget_input.text
        allocations = {
            "Food": self.ids.food_input.text,
            "Transport": self.ids.transport_input.text,
            "Utilities": self.ids.utilities_input.text,
            "Entertainment": self.ids.entertainment_input.text,
            "Other": self.ids.other_input.text,
        }
        print(f"Monthly Income: {income}")
        print(f"Monthly Budget: {budget}")
        print("Category Allocations:")
        for category, amount in allocations.items():
            print(f"  {category}: {amount}")
        # Add your backend logic here

class BudgetApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(BudgetScreen())
        return sm

if __name__ == "__main__":
    BudgetApp().run()