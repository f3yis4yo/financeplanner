from kivy.lang import Builder
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen
import os
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from models.database import Expense, get_session
from datetime import datetime

# Load the .kv file
kv_dir = os.path.dirname(__file__)
Builder.load_file(os.path.join(kv_dir, '../view/expenses.kv'))

class ExpensesScreen(Screen):
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

    def validate_inputs(self):
        expense_name = self.ids.expense_name_input.text.strip()
        amount = self.ids.amount_input.text.strip()
        category = self.ids.category_spinner.text
        date = self.ids.date_input.text.strip()

        if not expense_name:
            self.show_popup("Error", "Please enter an expense name")
            return False

        if not amount:
            self.show_popup("Error", "Please enter an amount")
            return False
        try:
            amount = float(amount)
            if amount <= 0:
                self.show_popup("Error", "Amount must be greater than zero")
                return False
        except ValueError:
            self.show_popup("Error", "Amount must be a valid number")
            return False

        if category == "Choose category":
            self.show_popup("Error", "Please select a category")
            return False

        if not date:
            self.show_popup("Error", "Please enter a date")
            return False
        try:
            datetime.strptime(date, '%Y-%m-%d')
        except ValueError:
            self.show_popup("Error", "Invalid date format. Use YYYY-MM-DD")
            return False

        return True

    def clear_inputs(self):
        self.ids.expense_name_input.text = ""
        self.ids.amount_input.text = ""
        self.ids.category_spinner.text = "Choose category"
        self.ids.date_input.text = ""
        self.ids.notes_input.text = ""

    def cancel(self):
        self.clear_inputs()
        self.show_popup("Cancelled", "Operation cancelled. All fields cleared.")
        self.manager.current = 'dashboard_screen'

    def submit_expense(self):
        if not self.validate_inputs():
            return

        try:
            user_id = 1  # Replace with actual logged-in user ID
            expense_name = self.ids.expense_name_input.text.strip()
            amount = float(self.ids.amount_input.text)
            category = self.ids.category_spinner.text
            date = datetime.strptime(self.ids.date_input.text, '%Y-%m-%d').date()
            print(date)
            notes = self.ids.notes_input.text.strip() if self.ids.notes_input.text else ""

            new_expense = Expense(
                user_id=user_id,
                expense_name=expense_name,
                amount=amount,
                category=category,
                date=date,
                notes=notes
            )

            self.session.add(new_expense)
            self.session.commit()

            self.show_popup("Success", "Expense added successfully!")
            self.clear_inputs()
            self.manager.current = 'dashboard_screen'

        except Exception as e:
            self.session.rollback()
            print(f"Error adding expense: {str(e)}")
            self.show_popup("Error", f"Error adding expense: {str(e)}")

        finally:
            self.session.close()

class ExpensesApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(ExpensesScreen())
        return sm

if __name__ == "__main__":
    ExpensesApp().run()