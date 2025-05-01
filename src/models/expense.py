from kivy.lang import Builder
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen
import os

# Load the .kv file
kv_dir = os.path.dirname(__file__)
Builder.load_file(os.path.join(kv_dir, '../view/expenses.kv'))

class ExpensesScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def submit_expense(self):
        # Placeholder for future functionality
        expense_name = self.ids.expense_name_input.text
        amount = self.ids.amount_input.text
        category = self.ids.category_spinner.text
        date = self.ids.date_input.text
        notes = self.ids.notes_input.text
        print(f"Expense submitted: {expense_name}, {amount}, {category}, {date}, {notes}")
        # Here you will add database interaction and navigation

class ExpensesApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(ExpensesScreen())
        return sm

if __name__ == "__main__":
    ExpensesApp().run()