from kivy.lang import Builder
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from models.encrypt import hash_password 
from models.database import engine, base, session, sessionActive, user
from kivy.uix.screenmanager import ScreenManager, Screen
import os

class MyGrid(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 3

    def submit_registration(self):
        fullname = self.ids.fullname_input.text
        email = self.ids.email_input.text
        phone = self.ids.phone_input.text
        password = hash_password(self.ids.password_input.text)
        confirm_password = self.ids.confirm_password_input.text
        security_question = self.ids.security_question_spinner.text
        security_answer = self.ids.security_answer_input.text
        terms_accepted = self.ids.terms_checkbox.active
        updates_subscribed = self.ids.updates_checkbox.active

        new_user = user(fullname = fullname, email = email, phone = phone, password = password, confirm_password = confirm_password, security_question = security_question, security_answer = security_answer, terms_accepted = terms_accepted, updates_subscribed = updates_subscribed) 
        sessionActive.add(new_user) # Add the new user object to the session
        try:
            sessionActive.commit() # Commit the changes to the database
            print("Adding a new user...")
        except Exception as e:
            sessionActive.rollback() # If an error occurs, rollback the transaction
            print("❌ Error adding user:", e) # Print the error message
        pass

class RegisterApp(App):
    def build(self):
        return MyGrid()

if __name__ == "__main__":
    RegisterApp().run()