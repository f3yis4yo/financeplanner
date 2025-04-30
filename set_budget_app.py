
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import sqlite3

# Set up the database
conn = sqlite3.connect('budget.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS budget (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        income REAL NOT NULL,
        budget_limit REAL NOT NULL
    )
''')
conn.commit()
conn.close()

# Kivy screen for setting budget
class BudgetScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=10, spacing=10, **kwargs)

        self.add_widget(Label(text="Enter Total Income:"))
        self.income_input = TextInput(multiline=False, input_filter='float')
        self.add_widget(self.income_input)

        self.add_widget(Label(text="Set Budget Limit:"))
        self.budget_input = TextInput(multiline=False, input_filter='float')
        self.add_widget(self.budget_input)

        self.save_button = Button(text="Save Budget")
        self.save_button.bind(on_press=self.save_budget)
        self.add_widget(self.save_button)

        self.message = Label(text="")
        self.add_widget(self.message)

    def save_budget(self, instance):
        try:
            income = float(self.income_input.text)
            budget = float(self.budget_input.text)

            conn = sqlite3.connect('budget.db')
            cursor = conn.cursor()
            cursor.execute('INSERT INTO budget (income, budget_limit) VALUES (?, ?)', (income, budget))
            conn.commit()
            conn.close()

            self.message.text = f"✅ Budget saved!\nIncome: ${income} | Limit: ${budget}"
        except ValueError:
            self.message.text = "❌ Please enter valid numbers."

# Launch the app
class BudgetApp(App):
    def build(self):
        return BudgetScreen()

if __name__ == '__main__':
    BudgetApp().run()
