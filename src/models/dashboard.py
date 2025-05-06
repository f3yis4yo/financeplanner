# dashboard.py
from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.metrics import dp
from models.database import get_session, User, Budget, Expense, get_current_budget, get_user_expenses
from kivy.properties import StringProperty
import os
from models.report_dashboard import ReportDashboard

class DashboardScreen(Screen):
    username = StringProperty('@User!')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.session = get_session()
        self.user_id = 1 # Replace with the actual logged-in user ID

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

    def on_enter(self):
        """update dashboard using current user data once logged in"""
        self.update_greeting()
        self.update_total_balanced()
        self.update_recent_expenses()
        self.update_notifications()

    def update_greeting(self):
        """update greeting with current name"""
        try:
            user = self.session.query(User).filter(User.fullname == self.username).first()
            if user:
                self.ids.greeting_label.text = f"Hello, {user.fullname}!"
            else:
                self.ids.greeting_label.text = f"Hello, {self.username}!"
        except Exception as e:
            print(f"Error updating greeting: {e}")

    def update_total_balanced(self):
        """calculate and show total balance"""
        try:
            # get most recent budget
            budget = get_current_budget(self.user_id)
            if not budget:
                self.ids.total_balance_label.text = "No budget set"
                return
            # calculate total expenses
            expenses = self.session.query(Expense).filter(Expense.user_id == self.user_id).all()
            total_expenses = sum(exp.amount for exp in expenses)

            #calculate total balance
            total_balance = budget.monthly_budget - total_expenses
            self.ids.total_balance_label.text = f"${total_balance:,.2f}"
        except Exception as e:
            print(f"Error updating total balance: {e}")

    def update_recent_expenses(self):
        """Display the 5 most recent expenses"""
        try:
            expenses = (
                self.session.query(Expense)
                .filter(Expense.user_id == self.user_id)
                .order_by(Expense.date.desc())
                .limit(5)
                .all()
            )
            if not expenses:
                self.ids.recent_expenses_label.text = "No recent expenses"
            else:
                recent_expenses_text = "\n".join(
                [f"{exp.category}: ${exp.amount:,.2f}" for exp in expenses]
            )
            self.ids.recent_expenses_label.text = recent_expenses_text or "No recent expenses"
        except Exception as e:
            print(f"Error updating recent expenses: {e}")

    def update_notifications(self):
        """Display notifications based on budget limit and expenses"""
        try:
            # get most recent budget
            budget = get_current_budget(self.user_id)
            if not budget:
                self.ids.notifications_label.text = "No budget at this time"
                return
            # calculate total expenses
            expenses = self.session.query(Expense).filter(Expense.user_id == self.user_id).all()
            total_expenses = sum(exp.amount for exp in expenses)
            #create notification messages
            notifications = []
            if total_expenses >= 0.5 * budget.monthly_budget:
                notifications.append(" Be careful you have spent over 50% of your budget")
            if total_expenses >= 0.8 * budget.monthly_budget:
                notifications.append(" Warning you have spent over 80% of your budget")
            if total_expenses > budget.monthly_budget:
                notifications.append(" Failed you have exceeded your budget!")

            #Display notifications
            self.ids.notifications_label.text = "\n".join(notifications) or "No Notifications at this moment"
        except Exception as e:
            print(f"Error updating notifications: {e}")

    def logout(self):
        """Handles user logout"""
        print("Logging out...")
        App.get_running_app().stop()

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