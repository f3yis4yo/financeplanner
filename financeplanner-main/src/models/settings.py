# settings.py
from kivy.app import App
from kivy.uix.screenmanager import Screen
from models.encrypt import hash_password
from models.database import get_session, User
from kivy.properties import StringProperty


class MySettings(Screen):  # Inherit directly from Screen
    current_user_email = StringProperty("")
    login_error = StringProperty("")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def save_new_password(self): # Add 'instance' as the first argument.
        self.login_error = ''
        new_password = self.ids.new_password_input.text
        print(new_password)
        confirm_password = self.ids.confirm_new_password_input.text

        if new_password == confirm_password:
            if self.current_user_email:
                session = get_session()
                try:
                    user_to_update = session.query(User).filter(User.email == self.current_user_email).first()
                    print(user_to_update)
                    if user_to_update:
                        hashed_new_password = hash_password(new_password)
                        user_to_update.password = hashed_new_password
                        session.commit()
                        print(f"✅ Password updated successfully for user: {self.current_user_email}")
                        self.manager.current = 'login_screen'  # Go back to the login screen
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
