from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.metrics import dp
from kivy.graphics import Color, Rectangle

class MySettings(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.rows = 8

        # Background color
        with self.canvas.before:
            Color(0.83, 0.83, 0.83, 1)  #LIGHT GREY 
            self.bg_rect = Rectangle(pos=self.pos, size=self.size)
        self.bind(pos=self._update_bg, size=self._update_bg)

        # Row A: Title
        row_a = GridLayout (cols=1)
        label_a = (Label(
            text='Settings',
            halign = 'center',
            font_size=24,
            bold=True,
            color=(0, 0, 0, 1),
        )) 
        row_a.add_widget(label_a)
        self.add_widget(row_a)

        # Row B: Subtitle "Edit Profile"
        row_b = GridLayout(cols=1)
        label_b =(Label(
            text='Edit Profile',
            halign = 'center',
            font_size = 18,
            bold=True,
            color=(0.2, 0.4, 1, 1), # BLUE
        )) 
        row_b.add_widget(label_b)
        self.add_widget(row_b)

        # Row C: BoxLayout for user input fields
        row_c = GridLayout (cols = 1, size_hint_y=3)
        input_box = BoxLayout(orientation='vertical', size_hint=(1, None), height=dp(180), padding=dp(8), spacing=dp(6))
        with input_box.canvas.before:
            Color(1, 1, 1, 1)
            self.input_bg = Rectangle(pos=input_box.pos, size=input_box.size)
        input_box.bind(pos=lambda instance, value: setattr(self.input_bg, 'pos', value),
                       size=lambda instance, value: setattr(self.input_bg, 'size', value))
        input_box.add_widget(self.create_input_row('Full Name:'))
        input_box.add_widget(self.create_input_row('Email:'))
        input_box.add_widget(self.create_input_row('Phone:'))
        input_box.add_widget(self.create_input_row('Address:'))
        row_c.add_widget(input_box)
        self.add_widget(row_c)

        # Row D: Buttons (Cancel and Save)
        row_d = GridLayout(cols=3, size_hint_y = None, height = dp(30))
        row_d.add_widget(Button(
            text='Cancel',
            halign = 'left',
            background_color=(0.66, 0.66, 0.66, 1),
            on_press=self.cancel_action
        ))  
        row_d.add_widget(Label(text=''))# empty D2
        row_d.add_widget(Button(
            text='Save',
            halign = 'right',
            background_color=(0.2, 0.5, 1, 1),
            on_press=self.save_action
        )) 
        self.add_widget(row_d)

        # Row E: Subtitle "Change Password"
        row_e = GridLayout(cols=1)
        label_e = (Label(
            text ='Change Password',
            halign = 'center',
            font_size = 18,
            bold=True,
            color=(0.2, 0.4, 1, 1),
        ))  
        row_e.add_widget(label_e)
        self.add_widget(row_e)

        # Row F: BoxLayout for password fields
        row_f = GridLayout(cols=1, size_hint_y=3)
        password_box = BoxLayout(
            orientation='vertical', 
            size_hint=(1, None), 
            height=dp(140), 
            padding=dp(8), spacing=dp(6))
        with password_box.canvas.before:
            Color(1, 1, 1, 1)
            self.password_bg = Rectangle(pos=password_box.pos, size=password_box.size)
        password_box.bind(pos=lambda instance, value: setattr(self.password_bg, 'pos', value),
                          size=lambda instance, value: setattr(self.password_bg, 'size', value))
        password_box.add_widget(self.create_input_row('Current Password:', password=True))
        password_box.add_widget(self.create_input_row('New Password:', password=True))
        password_box.add_widget(self.create_input_row('Confirm New Password:', password=True))
        row_f.add_widget(password_box)  
        self.add_widget(row_f)

        # Row G: Buttons (Cancel and Save)
        row_g = GridLayout(cols=3, size_hint_y = None, height = dp(30))
        row_g.add_widget(Button(
            text='Cancel',
            halign = 'left',
            background_color=(0.66, 0.66, 0.66, 1),
            on_press=self.cancel_action
        ))  
        row_g.add_widget(Label(text='')) # empty G2
        row_g.add_widget(Button(
            text='Save',
            halign = 'right',
            background_color=(0.2, 0.5, 1, 1),
            on_press=self.save_action
        )) 
        self.add_widget(row_g)
    
    # function as helper to create input rows with labels and text inputs \ password = false means 
    def create_input_row(self, label_text, password=False):
        row = BoxLayout(
            orientation='horizontal', 
            size_hint=(1, None), 
            height=dp(36), 
            spacing=dp(6))
        row.add_widget(Label(
            text=label_text,
            font_size = 14,
            color=(0, 0, 0, 1),
            size_hint_x = 0.4
        ))
        row.add_widget(TextInput(
            password = password,
            multiline = False, # allows only one line to input text
            size_hint_x = 0.6
        ))
        return row
    
    # function to update the backgoround rectangle when the size or position changes
    def _update_bg(self, *args):
        self.bg_rect.pos = self.pos
        self.bg_rect.size = self.size
    
    # instance method for cancel action TBD
    def cancel_action(self, instance):
        print("Cancel action triggered")
    
    # instance method for save action TBD
    def save_action(self, instance):
        print("Save action triggered")

class SettingsApp(App):
    def build(self):
        return MySettings()

if __name__ == '__main__':
    SettingsApp().run()