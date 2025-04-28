import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.graphics import Color, RoundedRectangle, Rectangle
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.lang import Builder
import os
from models.expenses import AddExpensePopup
from models.predictions import PredictionApp
from models.register import MyGrid as RegisterScreen
from models.login import MyLogin
from models.recover import MyRecover as RecoverScreen

# Define las rutas a los archivos KV
kv_dir = os.path.dirname(__file__)
login_kv_path = os.path.join(kv_dir, "view", "loginapp.kv")
register_kv_path = os.path.join(kv_dir, "view", "registerapp.kv")
recover_kv_path = os.path.join(kv_dir, "view", "recoverapp.kv")

try:
    Builder.load_file(login_kv_path)
    Builder.load_file(register_kv_path)
    Builder.load_file(recover_kv_path)
except FileNotFoundError as e:
    print(f"Error: KV file not found: {e}")

class CustomGrid(GridLayout):
    pass

class FinancePlannerApp(App):
    def build(self):
        Window.clearcolor = (0.95, 0.95, 0.95)
        sm = ScreenManager()
        login_screen = MyLogin(name='login_screen')
        register_screen = RegisterScreen(name='register_screen')
        recover_screen = RecoverScreen(name='recover_screen')
        sm.add_widget(login_screen)
        sm.add_widget(register_screen)
        sm.add_widget(recover_screen)
        return sm

if __name__ == '__main__':
    FinancePlannerApp().run()