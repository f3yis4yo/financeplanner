from kivy.lang import Builder
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
import os

# Define la ruta al archivo KV
kv_file_path = os.path.join(os.path.dirname(__file__), "..", "view", "registerapp.kv")

try:
    Builder.load_file(kv_file_path)
except FileNotFoundError:
    print(f"Error: No se encontró el archivo KV en: {kv_file_path}")

class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def submit_registration(self):
        fullname = self.ids.fullname_input.text
        email = self.ids.email_input.text
        phone = self.ids.phone_input.text
        password = self.ids.password_input.text
        confirm_password = self.ids.confirm_password_input.text
        security_question = self.ids.security_question_spinner.text
        security_answer = self.ids.security_answer_input.text
        terms_accepted = self.ids.terms_checkbox.active
        updates_subscribed = self.ids.updates_checkbox.active

        print("--- Datos de Registro ---")
        print(f"Nombre completo: {fullname}")
        print(f"Email: {email}")
        print(f"Teléfono: {phone}")
        print(f"Contraseña: {password}")
        print(f"Confirmar contraseña: {confirm_password}")
        print(f"Pregunta de seguridad: {security_question}")
        print(f"Respuesta de seguridad: {security_answer}")
        print(f"Acepta términos: {terms_accepted}")
        print(f"Subscrito a actualizaciones: {updates_subscribed}")
        print("-------------------------")
        pass

class RegisterApp(App):
    def build(self):
        return MyGrid()

if __name__ == "__main__":
    RegisterApp().run()