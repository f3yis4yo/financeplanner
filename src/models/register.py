from kivy.lang import Builder
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from models.encrypt import hash_password
from models.database import engine, base, user, get_session  # Import get_session
from kivy.uix.screenmanager import ScreenManager, Screen
import os


class MyGrid(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def submit_registration(self):
        fullname = self.ids.fullname_input.text
        email = self.ids.email_input.text
        phone = self.ids.phone_input.text
        password = hash_password(self.ids.password_input.text)
        confirm_password = self.ids.confirm_password_input.text
        security_question = self.ids.security_question_spinner.text
        security_answer = self.ids.security_answer_input.text
        terms_accepted = 'True' if self.ids.terms_checkbox.active else 'False'
        updates_subscribed = 'True' if self.ids.updates_checkbox.active else 'False'

        session = get_session()  # Obtén una nueva sesión
        try:
            new_user = user(
                fullname=fullname,
                email=email,
                phone=phone,
                password=password,
                confirm_password=confirm_password,
                security_question=security_question,
                security_answer=security_answer,
                terms_accepted=terms_accepted,
                updates_subscribed=updates_subscribed
            )
            session.add(new_user)
            session.commit()
            print("✅ User registered successfully!")
            self.manager.current = 'login_screen' 
        except Exception as e:
            session.rollback()
            print(f"❌ Error during registration: {e}")
        finally:
            session.close()

class RegisterApp(App):
    def build(self):
        return MyGrid()

if __name__ == "__main__":
    RegisterApp().run()