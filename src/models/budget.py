from kivy.lang import Builder
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
import os
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from models.database import Budget, BudgetAllocation, get_session
from datetime import datetime

# Load the .kv file
kv_dir = os.path.dirname(__file__)
Builder.load_file(os.path.join(kv_dir, '../view/budget.kv'))

class BudgetScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.session = get_session()

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
            user_id = 1  # Replace with actual logged-in user ID
            income = float(self.ids.income_input.text)
            budget = float(self.ids.budget_input.text)
            allocations = {
                "Food": float(self.ids.food_input.text),
                "Transport": float(self.ids.transport_input.text),
                "Utilities": float(self.ids.utilities_input.text),
                "Entertainment": float(self.ids.entertainment_input.text),
                "Other": float(self.ids.other_input.text),
            }

            # Create new budget
            new_budget = Budget(
                user_id=user_id,
                monthly_income=income,
                monthly_budget=budget,
                start_date=datetime.now().date()
            )
            self.session.add(new_budget)
            self.session.flush()  # This will set the id of new_budget

            # Create budget allocations
            for category, amount in allocations.items():
                allocation = BudgetAllocation(
                    budget_id=new_budget.id,
                    category=category,
                    amount=amount
                )
                self.session.add(allocation)

            self.session.commit()
            self.show_popup("Success", "Budget saved successfully!")
            self.clear_inputs()
            self.manager.current = 'dashboard_screen'

        except Exception as e:
            self.session.rollback()
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