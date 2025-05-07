from kivy.lang import Builder
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
import os
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from models.database import Budget, BudgetAllocation, get_session, update_or_create_budget, get_current_budget
from datetime import datetime

# Load the .kv file
kv_dir = os.path.dirname(__file__)
Builder.load_file(os.path.join(kv_dir, '../view/budget.kv'))

class BudgetScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.session = get_session() 

    def on_pre_enter(self, *args):
        # pre-fill form with current budget if exists
        try:
            current_budget = get_current_budget(user_id = App.get_running_app().user_id ) # actual logged-in user ID and session
            if current_budget:
                self.ids.income_input.text = str(current_budget.monthly_income)
                self.ids.budget_input.text = str(current_budget.monthly_budget)

                #pre-fill allocations ******CHECK THIS****
                for allocation in current_budget.allocations:
                    if allocation.category == "Food":
                        self.ids.food_input.text = str(allocation.amount)
                    elif allocation.category == "Transport":
                        self.ids.transport_input.text = str(allocation.amount)
                    elif allocation.category == "Utilities":
                        self.ids.utilities_input.text = str(allocation.amount)
                    elif allocation.category == "Entertainment":
                        self.ids.entertainment_input.text = str(allocation.amount)
                    elif allocation.category == "Other":
                        self.ids.other_input.text = str(allocation.amount) 
        except Exception as e:
            print(f"Error pre-filling budget: {e}")

    def show_popup(self, title, message):
        popup = Popup(
            title=title,
            content=Label(text=message),
            size_hint=(None, None),
            size=(400, 200)
        )
        popup.open()

    def clear_inputs(self):
        self.ids.income_input.text = ""
        self.ids.budget_input.text = ""
        self.ids.food_input.text = ""
        self.ids.transport_input.text = ""
        self.ids.utilities_input.text = ""
        self.ids.entertainment_input.text = ""
        self.ids.other_input.text = ""

    def cancel(self):
        self.clear_inputs()
        self.show_popup("Cancelled", "Operation cancelled. All fields cleared.")
        self.manager.current = 'dashboard_screen'

    def validate_inputs(self):
        try:
            income = self.ids.income_input.text
            budget = self.ids.budget_input.text
            allocations = {
                "Food": self.ids.food_input.text,
                "Transport": self.ids.transport_input.text,
                "Utilities": self.ids.utilities_input.text,
                "Entertainment": self.ids.entertainment_input.text,
                "Other": self.ids.other_input.text,
            }

            # Validate income
            if not income:
                self.show_popup("Error", "Please enter monthly income")
                return False
            income = float(income)
            if income <= 0:
                self.show_popup("Error", "Income must be greater than zero")
                return False

            # Validate budget
            if not budget:
                self.show_popup("Error", "Please enter monthly budget")
                return False
            budget = float(budget)
            if budget <= 0:
                self.show_popup("Error", "Budget must be greater than zero")
                return False
            if budget > income:
                self.show_popup("Error", "Budget cannot exceed income")
                return False

            # Validate allocations
            total_allocation = 0
            for category, amount in allocations.items():
                if not amount:
                    self.show_popup("Error", f"Please enter amount for {category}")
                    return False
                try:
                    amount = float(amount)
                    if amount < 0:
                        self.show_popup("Error", f"Amount for {category} cannot be negative")
                        return False
                    total_allocation += amount
                except ValueError:
                    self.show_popup("Error", f"Invalid amount for {category}")
                    return False

            if abs(total_allocation - budget) > 0.01:  # Use a small tolerance
                self.show_popup("Error", f"Total allocations (${total_allocation:.2f}) must equal budget (${budget:.2f})")
                return False

            return True

        except ValueError:
            self.show_popup("Error", "Please enter valid numbers")
            return False

    def save_allocation(self):
        if not self.validate_inputs():
            return

        try:
            user_id = App.get_running_app().user_id  # actual logged-in user ID
            income = float(self.ids.income_input.text)
            budget = float(self.ids.budget_input.text)
            allocations = {
                "Food": float(self.ids.food_input.text),
                "Transport": float(self.ids.transport_input.text),
                "Utilities": float(self.ids.utilities_input.text),
                "Entertainment": float(self.ids.entertainment_input.text),
                "Other": float(self.ids.other_input.text),
            }
            # Helper fucntion to get current budget 
            update_or_create_budget(self.session, user_id, income, budget, allocations)
            self.show_popup("Success", "Budget updated successfull \n& Previous Expenses cleared")
            self.clear_inputs()
            self.manager.current = 'dashboard_screen'
        except Exception as e:
            self.show_popup("Error", f"Error saving budget: {str(e)}")
        finally:
            self.session.close()


class BudgetApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(BudgetScreen())
        return sm

if __name__ == "__main__":
    BudgetApp().run()