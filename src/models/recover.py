from kivy.lang import Builder
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from models.encrypt import hash_password
from models.database import get_session, user
from kivy.uix.screenmanager import ScreenManager, Screen
import os


class MyRecover(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def submit_recovery(self):
        email = self.ids.email_recover_input.text
        security_question = self.ids.security_question_recover_spinner.text
        security_answer = self.ids.security_answer_recover_input.text

        session = get_session()  # Obtén una nueva sesión
        try:
            # Lógica para buscar el usuario por email y pregunta de seguridad
            found_user = session.query(user).filter(user.email == email, user.security_question == security_question, user.security_answer == security_answer).first()

            if found_user:
                print(f"✅ Recovery initiated for user: {found_user.email}")
                # Aquí iría la lógica para generar un enlace de recuperación
                # o permitir restablecer la contraseña.
            else:
                print("❌ Recovery information incorrect.")

            session.commit() # Consider when to commit based on your recovery logic
        except Exception as e:
            session.rollback()
            print(f"❌ Error during password recovery attempt: {e}")
        finally:
            session.close()

if __name__ == "__main__":
    class RecoverApp(App):
        def build(self):
            return MyRecover()
    RecoverApp().run()