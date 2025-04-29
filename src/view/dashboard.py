from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.metrics import dp
from kivy.graphics import Color, Rectangle, RoundedRectangle
import os
#from models.expenses import AddExpensePopup
#from models.predictions import PredictionApp
#from models.register import MyGrid 
#from models.login import MyLogin 
#from models.settings import MySettings
#from models.expenses import SummaryPopup


"""CustumGrid in github instead of DashboardScreen"""
class DashboardScreen(GridLayout):
    # The main screen of app, dashboard layout 
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.rows = 14 # Number of rows grid layout (A-L) / 3 for spaces
#        self.prediction_app = PredictionApp() # Instantiate PredictionApp and store it as an instance attribute.
#        self.prediction_app.bind(on_predictions=self.handle_predictions) # Bind the 'on_predictions' event to the 'handle_predictions' method.

        # App background color
        with self.canvas.before: 
            Color(0.83, 0.83, 0.83, 1)  #LIGHT GREY 
            self.rect = Rectangle(
                size=self.size, 
                pos=self.pos    # background rectangle size and position
                ) 
        self.bind(
            size=self.update_rect, 
            pos=self.update_rect   # bind is update rect size and position as the app resizes
            ) 
        
        # Row A: Title "BudgieBudget"
        row_a = GridLayout(cols = 1, size_hint_y = None, height = dp(40))
        row_a.add_widget(Label(
            text='BudgieBudget',
            halign = 'center',
            color = (0,0,0,1), #black
            bold=True, 
            font_size=24, 
        ))
        self.add_widget(row_a)

        # Row B: Subtitle "Dashboard"
        row_b = GridLayout(cols=1, size_hint_y = None, height = dp(30))
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
            size_hint_y = 0.5,
            height = dp(30),
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
        # settings for setting button as rounded btn 
        settings_btn = Button(
            text='SET', #'⚙️'
            halign = 'right',
            font_size = 15,  # Reduced font size
            size_hint = (None, None),
            size = (dp(50), dp(30)),
            on_press=self.open_settings,
            background_normal = '', # remove default background
            background_color = (0.5, 0.5, 0.5, 1) # light blue
            )
        with settings_btn.canvas.before:
            Color(0.5, 0.5, 0.5, 1)
            settings_btn.rect = RoundedRectangle( 
                pos=settings_btn.pos,
                size=settings_btn.size, 
                radius = [15],
            )
        settings_btn.bind(
            pos= lambda intance, val: setattr(settings_btn.rect,'pos',val),
            size = lambda instance, val: setattr(settings_btn.rect,'size',val))  
          
        row_c.add_widget(settings_btn)                                         
        self.add_widget(row_c)
        
        # Row D: Total Balance box (spans 1 columns, white background, double height)
        row_d = GridLayout(
            cols = 1,
            size_hint_y = None,
            height = dp(80) 
            )
        balance_box = BoxLayout(
            orientation = 'vertical',
            padding = 4, 
            size_hint = (1, 1), 
            )
        with balance_box.canvas.before:
            Color(1, 1, 1, 1)  # White
            self.balance_bg = RoundedRectangle(
                pos=balance_box.pos, 
                size=balance_box.size,
                radius = [10]
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

        #  Space total balance % func button
        row_d0 = GridLayout (cols = 1, size_hint_y = None, height = dp(10))
        row_d0.add_widget(Label(text = ''))
        self.add_widget(row_d0)

        # Row E: Main buttons (Add Expense, Set Budget, View Reports, Buttons)
        row_e = BoxLayout(orientation = 'horizontal', spacing = 30, padding = [20,0,20,0], size_hint_y = None, height = dp(110))
        # Add Expense button = d2_button (config)
        e2_btn_functions = self.make_icon_button(
            "➕",
            "Add \nExpense",
            (59/255, 130/255, 246/255, 1),
            self.show_add_expense_popup
            )
        row_e.add_widget(e2_btn_functions)
        e4_btn_functions = self.make_icon_button(
            "💰", 
            "Set \nBudget",
            (34/255, 211/255, 238/255, 1),
            self.go_to_set_budget
            )
        row_e.add_widget(e4_btn_functions)
        # View Report button = e3_button (config)
        e3_btn_functions = self.make_icon_button(
            "📊", 
            "View \nReports",
            (251/255, 191/255, 36/255, 1),
            self.show_add_summary_popup
            )
        row_e.add_widget(e3_btn_functions)
        self.add_widget(row_e)

        #  Space buttons % recent expenses
        row_e0 = GridLayout (cols = 1, size_hint_y = None, height = dp(30))
        row_e0.add_widget(Label(text = ''))
        self.add_widget(row_e0)

        # Row F: Recent Expenses Subtitle
        row_f = GridLayout(cols = 3, size_hint_y = None, height = dp(30))
        row_f.add_widget(Label(text='')) # empty F1
        row_f.add_widget(Label(
            text='Recent Expenses', 
            font_size = 18,
            bold = True,
            color = (0,0,0,1), #black
        ))
        row_f.add_widget(Label(text='')) #empty F3
        self.add_widget(row_f)

        # Row G: Recent Expenses->(box) => predictions
        row_g = GridLayout(cols = 1, size_hint_y = None, height = dp(60))
        expenses_box = BoxLayout(
            orientation='vertical', 
            size_hint=(1, 1), 
            padding = 8,
            )
        with expenses_box.canvas.before:
            Color(1, 1, 1, 1)  # gray
            self.expenses_bg = RoundedRectangle(
                pos=expenses_box.pos, 
                size=expenses_box.size,
                radius = [10],
                )
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
        row_g = GridLayout(cols=3, size_hint_y=3)
        row_g.add_widget(Label(size_hint_x=0.1)) # Add empty label for spacing.

        self.middle_label = Label(size_hint_x=0.8, color=(0, 0, 0, 1)) # Create the label for predictions, set text color to black.
        with self.middle_label.canvas.before:
            Color(1, 1, 1) # Set background color.
            self.middle_label.rect = Rectangle(size=self.middle_label.size, pos=self.middle_label.pos) # Create the background rectangle.
        self.middle_label.bind(size=self.update_rect, pos=self.update_rect) # Bind size and position changes to update_rect.
        row_g.add_widget(self.middle_label)

        row_g.add_widget(Label(size_hint_x=0.1)) # Add empty label for spacing.
        self.add_widget(row_g)
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
        row_i = GridLayout(cols = 1, size_hint_y = None, height = dp(60))
        notif_box = BoxLayout(
            orientation = 'vertical',
            padding = 8,
            size_hint = (1, 1), 
            ) 
        with notif_box.canvas.before:
            Color(1, 1, 1, 1)  # white
            self.notif_bg = RoundedRectangle(
                pos = notif_box.pos, 
                size = notif_box.size,
                radius = [10],
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
                'size', 
                value
                ))
        notif_box.add_widget(Label(
            text = 'No notifications at this time.', 
            font_size = 13, 
            color = (0,0,0,1)
            ))
        row_i.add_widget(notif_box)
        self.add_widget(row_i)


        # Row J: Space notification % logout button
        row_j = GridLayout (cols = 1, size_hint_y = None, height = dp(10))
        row_j.add_widget(Label(text = ''))
        self.add_widget(row_j)

        # Row K: Logout button (spans 3 columns)
        row_k = GridLayout(cols = 3, size_hint_y = None, height = dp(30))
        row_k.add_widget(Label(text='')) # empty J1
        logout_btn = (Button(
            text='Logout',
            font_size = 16,
            background_normal = '',
            background_color = (248/255, 113/255, 113/255, 1),  # #F87171
            color = (1, 1, 1, 1),
            on_press=self.logout,
        ))
        with logout_btn.canvas.before:
            Color(248/255, 113/255, 113/255, 1)
            logout_btn.rect = RoundedRectangle(
                pos = logout_btn.pos,
                size = logout_btn.size,
                radius = [10],
            )
        logout_btn.bind(
            pos=lambda instance, val: setattr(logout_btn.rect, 'pos', val),
            size=lambda instance, val: setattr(logout_btn.rect,'size', val))
        row_k.add_widget(logout_btn)    
        row_k.add_widget(Label(text=''))
        self.add_widget(row_k)
        
        # Row L: Year 2025
        row_l = BoxLayout(size_hint_y = None, height = dp(30))
        row_l.add_widget(Label(text=''))  # left space K1 (left)
        row_l.add_widget(Label(
            text='2025',
            color = (0,0,0,1),
            halign = 'center',
            ))  # year centered on position K2 
        row_l.add_widget(Label(text=''))  # left space K3 (right)
        self.add_widget(row_l)

    def update_rect(self, instance, value):
            self.rect.pos = self.pos
            self.rect.size = self.size
    
    def update_dark_rect(self, instance, value):
        with instance.canvas.after:
            instance.canvas.after.clear()
            Color(0, 0, 0, 0.3 if instance.state == 'down' else 0) # Set dark rectangle color based on button state.
            instance.dark_rect = RoundedRectangle(pos=instance.pos, size=instance.size, radius=[20, 20, 20, 20]) # Create dark rectangle.

    def make_icon_button(self, icon, text, bg_color, action):
        btn_functions = Button(
            text = f"{icon}\n{text}",
            font_size = 15,
            halign = 'center',
            valign = 'middle',
            background_normal = '',
            background_color = bg_color,
            color = (1, 1, 1, 1),
            size_hint = (None, None),
            size = (dp(100), dp(100)),
            on_press = action
        )
        with btn_functions.canvas.before:
            Color(*bg_color)
            btn_functions.rect = RoundedRectangle(pos=btn_functions.pos, size=btn_functions.size, radius=[10])
        btn_functions.bind(
            pos = lambda instance, val: setattr(btn_functions.rect, 'pos',val),
            size = lambda instance, val: setattr(btn_functions.rect, 'size', val)
            )
        return btn_functions

    def show_add_expense_popup(self, instance):
        print("Redirect to Add Expense screen")
#        popup = AddExpensePopup() # Create and open expense popup.
#        popup.open()
#        self.prediction_app.show_predictions()

    def go_to_set_budget(self, instance):
        print("Redirect to Set Budget screen")
 #       popup = SetBudgetPopup() # Create and open budget popup.
#        popup.open()
#        self.prediction_app.show_predictions() # Call PredictionApp to show prediction.

    def show_add_summary_popup(self, instance):
        print("Redirect to View Reports screen")
        #popup = SummaryPopup() # Create and open summary popup.
        #popup.open()

    def open_settings(self, instance):
        print("Open Settings menu")
#        popup = MySettings() # Create and open settings popup
#        popup.open()

    def logout(self, instance):
        print("Logging out...")
        App.get_running_app().stop() # Close the application.

    def show_add_predictions_popup(self, instance): #uses the recent
        print("Notificcations")
#        self.prediction_app.show_predictions() # Call PredictionApp to show predictions.

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
        
class BudgieBudget(App):
    def build(self):
        return DashboardScreen()

if __name__ == '__main__':
    BudgieBudget().run() 
