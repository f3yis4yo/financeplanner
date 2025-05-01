# recover.py
from kivy.lang import Builder
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner
from kivy.uix.button import Button
from models.database import get_session, user
from models.settings import MySettings
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import StringProperty
import os

class MyRecover(Screen):
    login_error = StringProperty('')
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def submit_recovery(self):
        self.login_error = ''
        email = self.ids.user_input.text
        security_question = self.ids.security_question_spinner.text
        security_answer = self.ids.confirm_password_input.text

        session = get_session()
        try:
            found_user = session.query(user).filter(
                user.email == email,
                user.security_question == security_question,
                user.security_answer == security_answer
            ).first()

            if found_user:
                print(f"✅ Recovery information correct for user: {found_user.email}")
                # Store the user's email
                self.manager.get_screen('settings_screen').current_user_email = email
                # Navigate to settings
                self.manager.current = 'settings_screen'
            else:
                self.login_error = "Recovery information incorrect."

        except Exception as e:
            print(f"❌ Error during password recovery attempt: {e}")
        finally:
            session.close()

if __name__ == "__main__":
    class RecoverApp(App):
        def build(self):
            # Use os.path.join to create paths, handle errors.
            kv_dir = os.path.dirname(__file__)
            recover_kv_path = os.path.join(kv_dir, '../view/recoverapp.kv')
            settings_kv_path = os.path.join(kv_dir, '../view/settingsapp.kv')

            # Load KV files, and check if they exist.
            try:
                if os.path.exists(recover_kv_path):
                    Builder.load_file(recover_kv_path)
                else:
                    raise FileNotFoundError(f"KV file not found: {recover_kv_path}")

                if os.path.exists(settings_kv_path):
                    Builder.load_file(settings_kv_path)
                else:
                    raise FileNotFoundError(f"KV file not found: {settings_kv_path}")

            except FileNotFoundError as e:
                print(f"Error: KV file not found: {e}")
                # It's crucial to raise the exception or return here
                # to prevent the app from continuing with missing UI.
                return  # Or raise the exception, depending on desired behavior

            # Create ScreenManager
            sm = ScreenManager()

            # Create screen instances. Crucially, do *not* pass the ScreenManager here.
            recover_screen = MyRecover(name='recover_screen')
            settings_screen = MySettings(name='settings_screen')

            # Add screens to ScreenManager
            sm.add_widget(recover_screen)
            sm.add_widget(settings_screen)

            return sm

    RecoverApp().run()
