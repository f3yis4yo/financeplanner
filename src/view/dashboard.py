from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.metrics import dp
from kivy.graphics import Color, Rectangle
#import os
#from models.expenses import AddExpensePopup
#from models.predictions import PredictionApp
#from models.register import MyGrid 
#from models.login import MyLogin 
#from models.settings import MySettings


"""CustumGrid in github instead of DashboardScreen"""
class CustumGrid(GridLayout):
    # The main screen of app, dashboard layout 
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.rows = 11 # Number of rows grid layout (A-K)
        #self.prediction_app = PredictionApp() # Instantiate PredictionApp and store it as an instance attribute.
        #self.prediction_app.bind(on_predictions=self.handle_predictions) # Bind the 'on_predictions' event to the 'handle_predictions' method.

        # App background color
        with self.canvas.before: 
            Color(0.83, 0.83, 0.83, 1)  #LIGHT GREY 
            self.rect = Rectangle(
                size=self.size, 
                pos=self.pos    # background rectangle size and position
                ) 
        self.bind(
            size=self._update_rect, 
            pos=self._update_rect   # bind is update rect size and position as the app resizes
            ) 
        
        # Row A: Title "BudgieBudget"
        row_a = GridLayout(cols = 1)
        row_a.add_widget(Label(
            text='BudgieBudget',
            halign = 'center',
            color = (0,0,0,1), #black
            bold=True, 
            font_size=24, 
        ))
        self.add_widget(row_a)

        # Row B: Subtitle "Dashboard"
        row_b = GridLayout(cols=1)
        label_b = Label(
            text = 'Dashboard',
            halign = 'center', 
            font_name = 'Arial', 
            font_size = 18, 
            bold = True,
            color = (0,0,0,1), #black
            )
        row_b.add_widget(label_b)
        self.add_widget(row_b)

        # Row C: C1 Hello @username!, C3 Settings button
        # Settings for label
        row_c = GridLayout(
            cols = 10, 
            size_hint_y = 0.5
            )
        row_c.add_widget(Label(text='')) # empty C1
        label_c = Label(
            text='Hello @Agustin!',
            halign = 'left',  
            font_name = 'Arial', 
            font_size = 15, 
            color = (0,0,0,1)#black
            )
        row_c.add_widget(label_c)
        for i in range(7):# fill remaining spaces
            row_c.add_widget(Label(text = '')) 
        # settings for setting button
        row_c.add_widget(Button(
            text='SET', #'⚙️'
            halign = 'right',
            font_size = 15,  # Reduced font size
            on_press=self.open_settings
            ))
        self.add_widget(row_c)
        
        # Row D: Total Balance box (spans 1 columns, white background, double height)
        row_d = GridLayout(
            cols = 1,
            size_hint_y = 3
            )
        balance_box = BoxLayout(
            orientation = 'vertical',
            padding = 4, 
            size_hint = (1, None), 
            height = 60)
        with balance_box.canvas.before:
            Color(1, 1, 1, 1)  # White
            self.balance_bg = Rectangle(
                pos=balance_box.pos, 
                size=balance_box.size
                )
        balance_box.bind(
            pos=lambda instance, 
            value: setattr(
                self.balance_bg, 
                'pos', value),
                size=lambda instance,
                value: setattr(
                self.balance_bg, 
                'size', value
                ))
        balance_box.add_widget(Label(
            text='Total Balance',
            font_size = 14,
            halign = 'left', 
            color=(0.2,0.4,1,1)
            ))
        balance_box.add_widget(Label(
            text = '$1,000',
            font_size = 22,
            bold=True,
            halign = 'right', 
            color=(0,0,0,1)
            ))
        row_d.add_widget(balance_box)
        self.add_widget(row_d)

        # Row E: Main buttons (Add Expense, Set Budget, View Reports, Buttons)
        row_e = GridLayout(cols = 5)
        row_e.add_widget(Label(text = '')) # empty E1
        # overall button config
        button_config = {
            'text_pos': 'buttom', #position of text in button
            'padding': (0, 90, 0, 0),  # padding is the space % the button text and image \ 0 padding on left, 90 on top, 0 on right, 0 on buttom 
            'image_&_offset': 20, # is the space % the image and text in button / 20 offset on y axis
            'size_hint': (0.9, 0.9) # makes all the buttons the same size (0.9 is 90% of the screen size)
            } 
        # Add Expense button = d2_button (config)
        e2_button = Button(
            text='➕\nAdd \nExpense',
            font_size = 15,
            background_color=(59/255, 130/255, 246/255, 1),  # #3B82F6
            )
        self.configure_rounded_button(
            e2_button, 
            'expenses.png', 
            **button_config # Configure button with image and text
            ) 
        e2_button.bind(on_press=self.show_add_expense_popup) # Bind expense button press.
        row_e.add_widget(self.create_button_box(e2_button))
        # Set Budget button = e4_button (config)
        e4_button = Button(
            text='💰\nSet \nBudget', 
            font_size = 15,
            background_color=(34/255, 211/255, 238/255, 1),  # #22D3EE
        )
        self.configure_rounded_button(
            e4_button,
            'predictions.png',                       # -> CHANGE IMAGE AND NAME TO budget.png
            **button_config) 
        e4_button.bind(                              # Bind prediction button press. 
            on_press=self.show_add_predictions_popup/# -> CHANGE on_press=self.go_to_set_budget
            ) 
        row_e.add_widget(self.create_button_box(e4_button))
        # View Report button = e3_button (config)
        e3_button = Button(
            text='📊\nView \nReports', 
            font_size = 15,
            background_color = (251/255, 191/255, 36/255, 1)) #FBBF24
        self.configure_rounded_button(
            e3_button,
            'summary.png',
            **button_config)
        e3_button.bind(on_press=self.show_add_summary_popup)
        row_e.add_widget(self.create_button_box(e3_button))
        row_e.add_widget(Label(text='')) # Add empty E5 for spacing.
        self.add_widget(row_e)

        # Row F: Recent Expenses Subtitle
        row_f = GridLayout(cols = 3)
        row_f.add_widget(Label(text='')) # empty F1
        row_f.add_widget(Label(
            text='Recent Expenses', 
            font_size = 18,
            bold = True,
            color = (0,0,0,1), #black
        ))
        row_f.add_widget(Label(text='')) #empty F3
        self.add_widget(row_f)

        # Row G: Recent Expenses->(box)
        row_g = GridLayout(cols = 1, size_hint_y = 3)
        expenses_box = BoxLayout(
            orientation='vertical', 
            size_hint=(1, None), 
            height = 60 )
        with expenses_box.canvas.before:
            Color(1, 1, 1, 1)  # gray
            self.expenses_bg = Rectangle(
                pos=expenses_box.pos, 
                size=expenses_box.size)
        expenses_box.bind(
            pos=lambda instance, 
            value: setattr(
                self.expenses_bg, 
                'pos', 
                value
                ),
            size=lambda instance, 
            value: setattr(
                self.expenses_bg, 
                'size', 
                value
                ))
        expenses_box.add_widget(Label(
            text = 'Groceries: $50', 
            font_size = 13, 
            color = (0,0,0,1)
            ))
        expenses_box.add_widget(Label(
            text = 'Transport: $20', 
            font_size = 13, 
            color = (0,0,0,1)
            ))
        row_g.add_widget(expenses_box)
        self.add_widget(row_g)

        """
        # Row C->G: Middle row with colored background for predictions.
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
        """
    
        # Row H: Notificationa Subtitle
        row_h = GridLayout(cols = 3)
        row_h.add_widget(Label(text='')) # empty H1
        row_h.add_widget(Label(
            text='Notifications', 
            font_size = 18,
            bold = True,
            color = (0,0,0,1), #black
        ))
        row_h.add_widget(Label(text='')) # empty H3
        self.add_widget(row_h)
      
        # Row I: Notifications-> box
        row_i = GridLayout(cols = 1, size_hint_y = 3)
        notif_box = BoxLayout(
            orientation = 'vertical',
            padding = 8, 
            size_hint = (1, None),
            height = 60
            )
        with notif_box.canvas.before:
            Color(1, 1, 1, 1)  # white
            self.notif_bg = Rectangle(
                pos = notif_box.pos, 
                size = notif_box.size
                )
        notif_box.bind(
            pos=lambda instance, 
            value: setattr(
                self.notif_bg, 
                'pos', 
                value
                ),
            size=lambda instance, 
            value: setattr(
                self.notif_bg,
                'size', value
                ))
        notif_box.add_widget(Label(
            text = 'No notifications at this time.', 
            font_size = 13, 
            color = (0,0,0,1)
            ))
        row_i.add_widget(notif_box)
        self.add_widget(row_i)

        # Row J: Logout button (spans 3 columns)
        row_j = GridLayout(cols = 3)
        row_j.add_widget(Label(text='')) # empty J1
        row_j.add_widget(Button(
            text='Logout',
            background_color = (248/255, 113/255, 113/255, 1),  # #F87171
            font_size = 16,
            on_press=self.logout
        ))
        row_j.add_widget(Label(text=''))
        self.add_widget(row_j)
        
        """
        close_button = Button()
        close_button.bind(on_press=self.close_app) # Bind close button press to close_app method.
        self.configure_rounded_button(close_button, image_name='power.png', apply_background=False) # Configure the close button.
        row_j.add_widget(close_button)
        self.add_widget(row_j)
        """

        # Row K: Year 2025
        row_k = BoxLayout()
        row_k.add_widget(Label(text=''))  # left space K1 (left)
        row_k.add_widget(Label(
            text='2025',
            color = (0,0,0,1)
            ))  # year centered on position K2 
        row_k.add_widget(Label(text=''))  # left space K3 (right)
        row_k.children[1].halign = 'center'  # Adjust year label to center 
        self.add_widget(row_k)

    def _update_rect(self, instance, value):
        if hasattr(instance, 'rect'):
        self.rect.pos = instance.pos
        self.rect.size = instance.size
    
    def update_dark_rect(self, instance, value):
        with instance.canvas.after:
            instance.canvas.after.clear()
            Color(0, 0, 0, 0.3 if instance.state == 'down' else 0) # Set dark rectangle color based on button state.
            instance.dark_rect = RoundedRectangle(pos=instance.pos, size=instance.size, radius=[20, 20, 20, 20]) # Create dark rectangle.

    def configure_rounded_button(self, button, image_name=None, text_pos='top', padding=(0, 0, 0, 0), image_&_offset=0, size_hint=(1, 1), apply_background=True):
        button.color = (0, 0, 0, 1)
        button.background_color = (1, 0, 0, 0) if apply_background else (1, 0, 1, 0)
        button.background_normal = ''
        button.background_down = ''
        button.text_pos = ('center', text_pos)
        button.padding = padding
        button.image_y_offset = image_&_offset
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

    def show_add_expense_popup(self, instance):
        print("Redirect to Add Expense screen")
        popup = AddExpensePopup() # Create and open expense popup.
        popup.open()
        self.prediction_app.show_predictions()

"""
    def go_to_set_budget(self, instance):
        print("Redirect to Set Budget screen")
        popup = SetBudgetPopup() # Create and open budget popup.
        popup.open()
        # self.prediction_app.show_predictions() # Call PredictionApp to show prediction.
"""

    def show_add_summary_popup(self, instance):
        print("Redirect to View Reports screen")
        from models.expenses import SummaryPopup
        popup = SummaryPopup() # Create and open summary popup.
        popup.open()

    def open_settings(self, instance):
        print("Open Settings menu")
        from models.settings import MySettings
        popup = MySettings() # Create and open settings popup
        popup.open()

    def logout(self, instance):
        print("Logging out...")
        App.get_running_app().stop() # Close the application.

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
        
class MyApp(App):
    def build(self):
        return CustumGrid()

if __name__ == '__main__':
    MyApp().run() 
