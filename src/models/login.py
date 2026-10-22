from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from sqlalchemy.orm import sessionmaker
from kivy.lang import Builder # Import Builder
from .database import User, engine 
from .encrypt import verify_password, hash_password
from .dashboard import DashboardScreen
import os

# Create a sessionmaker, which is a factory for creating database sessions
Session = sessionmaker(bind=engine)

def get_session():
    return Session()

class MyLogin(Screen):
    login_error = StringProperty('')

    def do_login(self):
        fullname = self.ids.user_input.text
        password = self.ids.password_input.text
        self.login_error = ''

        session = get_session()
        try:
            found_user = session.query(User).filter(User.fullname == fullname).first()
            if found_user:
                if verify_password(password, found_user.password):
                    self.manager.current = 'dashboard_screen'
                else:
                    self.login_error = "Incorrect password."
            else:
                self.login_error = "User not found."
        except Exception as e:
            self.login_error = f"An error occurred during login: {e}"
            session.rollback()
        finally:
            session.close()

class LoginScreen(MyLogin): # Now inherits from MyLogin
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class MainMenuScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(Label(text='Menú Principal'))
        self.add_widget(layout)

class RegisterScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(Label(text='Pantalla de Registro'))
        self.add_widget(layout)

class DashboardScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(Label(text='Dashboard'))
        self.add_widget(layout)

class TestApp(App):
    def build(self):
        # Load KV file here
        Builder.load_file("loginapp.kv")
        sm = ScreenManager() 
        sm.add_widget(DashboardScreen(name='dashboard_screen'))
        sm.add_widget(LoginScreen(name='my_login'))
        sm.add_widget(MainMenuScreen(name='main_menu_screen'))
        sm.add_widget(RegisterScreen(name='register_screen'))
        return sm

if __name__ == "__main__":
    TestApp().run()