import kivy
from kivymd.app import MDApp
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
from kivy.uix.screenmanager import ScreenManager, Screen
from report_dashboard import ReportDashboard
import os
from models.expense import ExpensesScreen
from models.predictions import PredictionApp
from models.register import MyGrid as RegisterScreen
from models.login import MyLogin
from models.recover import MyRecover as RecoverScreen
from models.dashboard import DashboardScreen as Dashboard_Screen
from models.settings import MySettings
from models.report_dashboard import ReportDashboard
<<<<<<< HEAD
=======
from models.budget import BudgetScreen
>>>>>>> rebeca_cardenas


# Define las rutas a los archivos KV
kv_dir = os.path.dirname(__file__)
login_kv_path = os.path.join(kv_dir, "view", "loginapp.kv")
register_kv_path = os.path.join(kv_dir, "view", "registerapp.kv")
recover_kv_path = os.path.join(kv_dir, "view", "recoverapp.kv")
dashboard_kv_path = os.path.join(kv_dir, "view", "dashboardapp.kv")
<<<<<<< HEAD
settings_kv_path = os.path.join(kv_dir, '../view/settingsapp.kv')
report_kv_path = os.path.join(kv_dir, '../view/reportdashboardapp.kv')
=======
settings_kv_path = os.path.join(kv_dir, "view", "settingsapp.kv")
expense_kv_path = os.path.join(kv_dir,  "view", "expenses.kv")
report_kv_path = os.path.join(kv_dir, "view", "reportdashboardapp.kv")
budget_kv_path = os.path.join(kv_dir, "view", "budget.kv")

>>>>>>> rebeca_cardenas
try:
    Builder.load_file(login_kv_path)
    Builder.load_file(register_kv_path)
    Builder.load_file(recover_kv_path)
    Builder.load_file(dashboard_kv_path)
    Builder.load_file(settings_kv_path)
<<<<<<< HEAD
    Builder.load_file(report_kv_path)
=======
    Builder.load_file(expense_kv_path)
    Builder.load_file(report_kv_path)
    Builder.load_file(budget_kv_path)
>>>>>>> rebeca_cardenas
except FileNotFoundError as e:
    print(f"Error: KV file not found: {e}")

class CustomGrid():
    def build(self):
        return

class RegisterApp(App):
    def build(self):
        return MyGrid()

class LoginApp(App):
    def build(self):
        return MyLogin()

class FinancePlannerApp(MDApp):
    def build(self):
        Window.clearcolor = (0.95, 0.95, 0.95)
        sm = ScreenManager()
        login_screen = MyLogin(name='login_screen')
        register_screen = RegisterScreen(name='register_screen')
        recover_screen = RecoverScreen(name='recover_screen')
        dashboard_screen = Dashboard_Screen(name='dashboard_screen')
        settings_screen = MySettings(name='settings_screen')
<<<<<<< HEAD
        #report_screen = ReportDashboard(name= 'report_screen')

class ReportScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(ReportDashboard())
=======
        expenses_screen = ExpensesScreen(name='expenses_screen')
        #report_screen = ReportDashboard(name='report_screen')
        budget_screen = BudgetScreen(name='budget_screen')
>>>>>>> rebeca_cardenas
        sm.add_widget(login_screen)
        sm.add_widget(register_screen)
        sm.add_widget(recover_screen)
        sm.add_widget(dashboard_screen)
        sm.add_widget(settings_screen)
<<<<<<< HEAD
        sm.add_widget(ReportScreen(name= 'report_screen'))
        sm.add_widget(DashboardScreen(name='dashboard'))
=======
        sm.add_widget(expenses_screen)
        #sm.add_widget(report_screen)
        sm.add_widget(budget_screen)
>>>>>>> rebeca_cardenas
        return sm

if __name__ == '__main__':
    FinancePlannerApp().run()