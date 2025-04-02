import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.graphics import Color, RoundedRectangle, Rectangle
from kivy.uix.image import Image
from kivy.core.window import Window
import os
from models.expenses import AddExpensePopup
from models.predictions import PredictionApp

class CustomGrid(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.rows = 6
        self.prediction_app = PredictionApp() # Instantiate PredictionApp and store it as an instance attribute.
        self.prediction_app.bind(on_predictions=self.handle_predictions) # Bind the 'on_predictions' event to the 'handle_predictions' method.

        # Row A: Top row with close button.
        row_a = GridLayout(cols=9, size_hint_y=0.5)
        for i in range(7):
            row_a.add_widget(Label(text='')) # Add empty labels for spacing.

        close_button = Button()
        close_button.bind(on_press=self.close_app) # Bind close button press to close_app method.
        self.configure_rounded_button(close_button, image_name='power.png', apply_background=False) # Configure the close button.
        row_a.add_widget(close_button)
        self.add_widget(row_a)

        # Row B: Displays "Hi Ivan" text.
        row_b = BoxLayout(size_hint_x=1, orientation='horizontal')
        row_b.add_widget(Label(size_hint_x=0.1)) # Add empty label for centering.
        label_b = Label(halign='center', text='Hi Ivan', font_name='Arial', font_size=40, color=(0, 0, 0, 1), bold=True, size_hint_x=None) # Create the "Hi Ivan" label.
        row_b.add_widget(label_b)
        row_b.add_widget(Label()) # Add empty label for centering.
        self.add_widget(row_b)

        # Row C: Middle row with colored background for predictions.
        row_c = GridLayout(cols=3, size_hint_y=3)
        row_c.add_widget(Label(size_hint_x=0.1)) # Add empty label for spacing.

        self.middle_label = Label(size_hint_x=0.8, color=(0, 0, 0, 1)) # Create the label for predictions, set text color to black.
        with self.middle_label.canvas.before:
            Color(1, 1, 1) # Set background color.
            self.middle_label.rect = Rectangle(size=self.middle_label.size, pos=self.middle_label.pos) # Create the background rectangle.
        self.middle_label.bind(size=self.update_rect, pos=self.update_rect) # Bind size and position changes to update_rect.
        row_c.add_widget(self.middle_label)

        row_c.add_widget(Label(size_hint_x=0.1)) # Add empty label for spacing.
        self.add_widget(row_c)

        # Row T: spacer row
        row_t = GridLayout(cols=1, size_hint_y=0.05)
        self.add_widget(row_t)

        # Row D: Buttons for Expenses, Summary, and Predictions.
        row_d = GridLayout(cols=5)
        row_d.add_widget(Label(text='')) # Add empty label for spacing.

        button_config = {'text_pos': 'bottom', 'padding': (0, 90, 0, 0), 'image_y_offset': 20, 'size_hint': (0.9, 0.9)} # Button configuration.

        d2_button = Button(text='Expenses') #Budget Limitatioins
        self.configure_rounded_button(d2_button, 'expenses.png', **button_config)
        d2_button.bind(on_press=self.show_add_expense_popup) # Bind expense button press.
        row_d.add_widget(self.create_button_box(d2_button))

        d3_button = Button(text='Summary')
        self.configure_rounded_button(d3_button, 'summary.png', **button_config)
        row_d.add_widget(self.create_button_box(d3_button))

        d4_button = Button(text='Predictions')
        self.configure_rounded_button(d4_button, 'predictions.png', **button_config)
        d4_button.bind(on_press=self.show_add_predictions_popup) # Bind prediction button press.
        row_d.add_widget(self.create_button_box(d4_button))

        row_d.add_widget(Label(text='')) # Add empty label for spacing.
        self.add_widget(row_d)

        # Row E: Displays "2025" text.
        row_e = BoxLayout()
        row_e.add_widget(Label(text=''))
        row_e.add_widget(Label(text='2025', color=(0, 0, 0, 1), font_size=24))
        row_e.add_widget(Label(text=''))
        row_e.children[1].halign = 'center' # Center the "2025" label.
        self.add_widget(row_e)

    def show_add_expense_popup(self, instance):
        popup = AddExpensePopup() # Create and open expense popup.
        popup.open()
        self.prediction_app.show_predictions() 
    
    def show_add_summary_popup(self, instance):
        popup = AddExpensePopup() # Create and open summary popup.
        popup.open()

    def show_add_predictions_popup(self, instance):
        self.prediction_app.show_predictions() # Call PredictionApp to show predictions.

    def handle_predictions(self, instance, predictions):
        try:
            prediction_text = ""
            for category, amount in predictions.items():
                prediction_text += f"{category}: {amount}\n"
            self.middle_label.text = prediction_text # Update the middle label with prediction text.
            return True # Indicates success.
        except Exception as e:
            print(f"Error updating predictions: {e}")
            return False # Indicates failure.

    def close_app(self, instance):
        App.get_running_app().stop() # Close the application.

    def update_rect(self, instance, value):
        if hasattr(instance, 'rect'):
            instance.rect.pos = instance.pos
            instance.rect.size = instance.size # Update rectangle size and position.

    def update_dark_rect(self, instance, value):
        with instance.canvas.after:
            instance.canvas.after.clear()
            Color(0, 0, 0, 0.3 if instance.state == 'down' else 0) # Set dark rectangle color based on button state.
            instance.dark_rect = RoundedRectangle(pos=instance.pos, size=instance.size, radius=[20, 20, 20, 20]) # Create dark rectangle.

    def configure_rounded_button(self, button, image_name=None, text_pos='top', padding=(0, 0, 0, 0), image_y_offset=0, size_hint=(1, 1), apply_background=True):
        button.color = (0, 0, 0, 1)
        button.background_color = (1, 0, 0, 0) if apply_background else (1, 0, 1, 0)
        button.background_normal = ''
        button.background_down = ''
        button.text_pos = ('center', text_pos)
        button.padding = padding
        button.image_y_offset = image_y_offset
        button.size_hint = size_hint
        with button.canvas.before:
            if apply_background:
                Color(0.31, 0.94, 0.79, 1) # Set button background color.
                button.rect = RoundedRectangle(pos=button.pos, size=button.size, radius=[20, 20, 20, 20]) # Create rounded rectangle for button.
            if image_name:
                image_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "static", "image", image_name)
                button.image = Image(source=image_path, pos=(button.pos[0], button.pos[1] + image_y_offset), size=button.size) # Add image to button.
        button.bind(pos=self.update_rect, size=self.update_rect, state=self.update_dark_rect) # Bind button properties.
        if image_name:
            button.bind(pos=self.update_image_pos, size=self.update_image_size) # Bind image properties.

    def create_button_box(self, button):
        box = BoxLayout(padding=(10, 10, 10, 10), size_hint_x=0.4)
        box.add_widget(button)
        return box # Create a box layout for the button.

    def update_image_pos(self, instance, value):
        instance.image.pos = (instance.pos[0], instance.pos[1] + instance.image_y_offset) # Update image position.

    def update_image_size(self, instance, value):
        instance.image.size = instance.size # Update image size.

class FinancePlannerApp(App):
    def build(self):
        Window.clearcolor = (0.95, 0.95, 0.95) # Set window background color.
        return CustomGrid() # Return the CustomGrid layout.

if __name__ == '__main__':
    FinancePlannerApp().run() # Run the application.