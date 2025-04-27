from kivy.lang import Builder
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from models.encrypt import hash_password 
from models.database import engine, base, session, sessionActive, user
from kivy.uix.screenmanager import ScreenManager, Screen

class MyRecover(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

if __name__ == "__main__":
    pass 