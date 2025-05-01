# settings.py
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.metrics import dp
from kivy.graphics import Color, Rectangle
from kivy.uix.screenmanager import Screen
from models.encrypt import hash_password, verify_password
from models.database import get_session, user
from kivy.properties import StringProperty

class MySettings(Screen):  # Inherit directly from Screen
    current_user_email = ""
    login_error = StringProperty('')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = GridLayout(cols=1, padding=20, spacing=10)  # Create a GridLayout with 1 column

        # Title
        layout.add_widget(Label(text='Password Recovery', font_size=24, bold=True, color=(0, 0, 0, 1), size_hint_y=None, height='40dp'))
        layout.add_widget(Label(text='Enter New Password', font_size=18, color=(0.2, 0.4, 1, 1), size_hint_y=None, height='30dp'))

        # New Password Input
        new_password_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height='40dp', spacing='10dp')
        new_password_layout.add_widget(Label(text='New Password:', size_hint_x=0.4, color=(0, 0, 0, 1)))
        self.new_password_input = TextInput(hint_text='New Password', password=True, multiline=False, size_hint_x=0.6)
        new_password_layout.add_widget(self.new_password_input)
        layout.add_widget(new_password_layout)

        # Confirm New Password Input
        confirm_password_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height='40dp', spacing='10dp')
        confirm_password_layout.add_widget(Label(text='Confirm New Password:', size_hint_x=0.4, color=(0, 0, 0, 1)))
        self.confirm_new_password_input = TextInput(hint_text='Confirm New Password', password=True, multiline=False, size_hint_x=0.6)
        confirm_password_layout.add_widget(self.confirm_new_password_input)
        layout.add_widget(confirm_password_layout)

        # Buttons Layout
        buttons_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height='40dp', spacing='10dp')
        cancel_button = Button(text='Cancel', background_color=(0.66, 0.66, 0.66, 1), on_press=self.cancel_action)
        save_button = Button(text='Save New Password', background_color=(0.2, 0.5, 1, 1), on_press=self.save_new_password)
        buttons_layout.add_widget(cancel_button)
        buttons_layout.add_widget(save_button)
        layout.add_widget(buttons_layout)

        self.add_widget(layout) # Add the main GridLayout to the Screen

    def cancel_action(self, instance):
        self.manager.current = 'recover_screen'

    def save_new_password(self, instance):
        self.login_error = ''
        new_password = self.new_password_input.text
        confirm_password = self.confirm_new_password_input.text

        if new_password == confirm_password:
            if self.current_user_email:
                session = get_session()
                try:
                    user_to_update = session.query(user).filter(user.email == self.current_user_email).first()
                    if user_to_update:
                        hashed_new_password = hash_password(new_password)
                        user_to_update.password = hashed_new_password
                        session.commit()
                        print(f"✅ Password updated successfully for user: {self.current_user_email}")
                        self.manager.current = 'login_screen' # Go back to the login screen
                    else:
                        self.login_error = f"❌ User with email {self.current_user_email} not found."
                except Exception as e:
                    session.rollback()
                    print(f"❌ Error updating password: {e}")
                finally:
                    session.close()
            else:
                print("❌ No user email provided for password update.")
        else:
            print("❌ New passwords do not match.")

class SettingsApp(App):
    def build(self):
        return MySettings()

if __name__ == '__main__':
    SettingsApp().run()