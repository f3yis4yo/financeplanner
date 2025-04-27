import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.graphics import Color, RoundedRectangle, Rectangle
from kivy.uix.image import Image
from kivy.core.window import Window
import os
from models.expenses import AddExpensePopup
from models.predictions import PredictionApp
from models.register import MyGrid 
from models.login import MyLogin 

class CustomGrid():
    def build(self):
        return 

class RegisterApp(App):
    def build(self):
        return MyGrid() 

class LoginApp(App):
    def build(self):
        return MyLogin() 

class FinancePlannerApp(App):
    def build(self):
        Window.clearcolor = (0.95, 0.95, 0.95) # Set window background color.
        #######
        #I use this variable to call the view
        ######
        registerStatus = True
        if registerStatus == False:
            return CustomGrid() # Return the CustomGrid layout.
        else:
            """register_app_instance = RegisterApp() # Crea una instancia de RegisterApp
            return register_app_instance.build() # Llama al método build de la instancia para obtener el widget raíz
"""
            register_app_instance = LoginApp()
            return register_app_instance.build() 

if __name__ == '__main__':
    FinancePlannerApp().run() # Run the application.