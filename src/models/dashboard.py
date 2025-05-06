from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.metrics import dp
import os
from report_dashboard import ReportDashboard
from models.report_dashboard import ReportDashboard

class DashboardScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def update_rect(self, instance, value):
        pass

    def update_dark_rect(self, instance, value):
        pass

    def make_icon_button(self, icon, text, bg_color, action):
        pass

    def show_add_expense_popup(self, instance):
        print("Redirect to Add Expense screen")

    def go_to_set_budget(self, instance):
        print("Redirect to Set Budget screen")

    def show_add_summary_popup(self, instance):
        print("Opening Report Dashboard...")
        report_screen = self.manager.get_screen('report_screen')
        report_screen.update_report_data()  # Initialize/refresh data
        self.manager.current = 'report_screen'

    def open_settings(self, instance):
        print("Open Settings menu")

    def logout(self, instance):
        print("Logging out...")
        App.get_running_app().stop()

    def show_add_predictions_popup(self, instance):
        print("Notifications")

    def handle_predictions(self, instance, predictions):
        try:
            prediction_text = ""
            for category, amount in predictions.items():
                prediction_text += f"{category}: {amount}\n"
            if hasattr(self.ids, 'prediction_label'):
                self.ids.prediction_label.text = prediction_text
            return True
        except Exception as e:
            print(f"Error updating predictions: {e}")
            return False


class BudgieBudget(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(DashboardScreen(name='dashboard'))
        
        from kivy.uix.screenmanager import screen
        class ReportScreen(Screen):
            def __init__(self, **kwargs):
                super().__init__(**kwargs)
                self.add_widget(ReportDashboard())
                
            def update_report_data(self):
                """Refresh report data when screen is accessed"""
                self.children[0].sample_data = self.children[0].generate_sample_data()
                
        sm.add_widget(ReportScreen(name='report_screen))'))
        
        return sm

if __name__ == '__main__':
    BudgieBudget().run()