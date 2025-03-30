from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup

class AddExpensePopup(Popup):
    """
    This class creates a popup to add new expenses.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title = "Add Expense"
        self.size_hint = (None, None)
        self.size = (600, 450)  # Increase popup size for better usability.
        self.auto_dismiss = False # Prevent popup from closing when clicking outside.

        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Input for the expense amount.
        layout.add_widget(Label(text="Amount:"))
        self.amount_input = TextInput(
            hint_text="Enter amount",
            input_type='number',
            size_hint_y=None,
            height=50,
            font_size=20
        )

        # Input for the expense category.
        layout.add_widget(Label(text="Category:"))
        self.category_input = TextInput(
            hint_text="Enter category",
            size_hint_y=None,
            height=50,
            font_size=20
        )

        # Layout for submit and cancel buttons.
        buttons_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=40, spacing=10)
        submit_button = Button(text="Submit")
        cancel_button = Button(text="Cancel")

        # Bind button presses to their respective methods.
        submit_button.bind(on_press=self.submit)
        cancel_button.bind(on_press=self.cancel)

        buttons_layout.add_widget(submit_button)
        buttons_layout.add_widget(cancel_button)

        # Add input fields and buttons to the main layout.
        layout.add_widget(self.amount_input)
        layout.add_widget(self.category_input)
        layout.add_widget(buttons_layout)

        self.content = layout

    def submit(self, instance):
        """
        Handles the submission of the expense form.
        """
        amount_str = self.amount_input.text
        category = self.category_input.text
        message_popup = Popup(size_hint=(None, None), size=(200, 100)) # Popup for messages.

        try:
            amount = float(amount_str) # Try converting amount to float.
            if category:
                # In a real app, data would be saved to a database or file.
                print(f"Expense added: {amount} in {category}")
                message_popup.title = "Success"
                message_popup.content = Label(text=f"Expense added: {amount} in {category}")
                message_popup.open()
            else:
                message_popup.title = "Warning"
                message_popup.content = Label(text="Expense not added. Please provide category.")
                message_popup.open()

        except ValueError:
            message_popup.title = "Warning"
            message_popup.content = Label(text="Invalid amount entered.")
            message_popup.open()

        self.dismiss() # Close the popup after submission.

    def cancel(self, instance):
        """
        Closes the popup without saving.
        """
        self.dismiss()

if __name__ == '__main__':
    class ExpenseApp(App):
        """
        Main application class.
        """
        def build(self):
            layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
            add_button = Button(text="Add Expense")
            add_button.bind(on_press=self.show_add_expense_popup)
            layout.add_widget(add_button)
            return layout

        def show_add_expense_popup(self, instance):
            """
            Opens the AddExpensePopup.
            """
            popup = AddExpensePopup()
            popup.open()

    ExpenseApp().run()