
from kivy.lang import Builder
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from models.register import MyGrid 
import os

# Define la ruta al archivo KV
kv_file_path = os.path.join(os.path.dirname(__file__), "..", "view", "loginapp.kv")
register_kv_path = os.path.join(os.path.dirname(__file__), "..", "view", "registerapp.kv") 

try:
    Builder.load_file(kv_file_path)
    Builder.load_file(register_kv_path)
except FileNotFoundError:
    print(f"Error: KV file not found in: {kv_file_path}")

class MyLogin(Screen):
    pass

class MyGrid(Screen): ############  Cambiar el nombre
    pass

class ScreenAplication(App):
    def build(self):
        if ScreenManager():
            sm = ScreenManager()
            register_screen = MyGrid(name='register_screen')
            sm.add_widget(register_screen)
            return sm
        else:
            print("ScreenManager")
    
if __name__ == "__main__":
    LoginApp().run()