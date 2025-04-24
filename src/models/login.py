
from kivy.lang import Builder
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
import os

# Define la ruta al archivo KV
kv_file_path = os.path.join(os.path.dirname(__file__), "..", "view", "loginapp.kv")

try:
    Builder.load_file(kv_file_path)
except FileNotFoundError:
    print(f"Error: KV file not found in: {kv_file_path}")

class MyLogin(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class LoginApp(App):
    def build(self):
        return MyLogin()

if __name__ == "__main__":
    LoginApp().run()