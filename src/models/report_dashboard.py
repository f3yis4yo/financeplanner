from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.uix.scrollview import ScrollView
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle
from kivy.uix.image import Image
import matplotlib.pyplot as plt
from io import BytesIO
import os
from datetime import datetime
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
from kivy.uix.textinput import TextInput

class ReportDashboard(BoxLayout):
    def _init_(self, **kwargs):
        super()._init_(**kwargs)
        self.sample_data = self.generate_sample_data()

    def generate_sample_data(self):
        # Generate 30 days of sample data
        data = []
        for i in range(1, 31):
            date = f"2023-01-{i:02d}"
            metric_a = 100 + i * 3
            metric_b = 200 - i * 2
            metric_c = 50 + i
            data.append({
                'date': date,
                'metric_a': metric_a,
                'metric_b': metric_b,
                'metric_c': metric_c
            })
        return data

    def apply_filters(self):
        month = self.ids.month_spinner.text
        from_date = self.ids.from_date.text
        to_date = self.ids.to_date.text

        # Validate dates
        try:
            if from_date:
                datetime.strptime(from_date, '%d/%m/%Y')
            if to_date:
                datetime.strptime(to_date, '%d/%m/%Y')
        except ValueError:
            self.show_popup("Invalid Date", "Please enter dates in DD/MM/YYYY format")
            return

        self.show_popup("Filters Applied",
                       f"Month: {month}\nFrom: {from_date}\nTo: {to_date}\n\n(Filter logic would be implemented here)")

    def download_report(self):
        # In a real app, this would generate a file
        self.show_popup("Download", "Report would be downloaded based on current filters")

        # This is how you would save a file in a real implementation:
        # with open("report.csv", "w") as f:
        #     f.write("Date,Metric A,Metric B,Metric C\n")
        #     for item in self.filtered_data():
        #         f.write(f"{item['date']},{item['metric_a']},{item['metric_b']},{item['metric_c']}\n")

    def show_graph(self):
        self.ids.content_area.clear_widgets()

        # Generate a matplotlib graph
        dates = [item['date'][-2:] for item in self.sample_data]  # Just show day numbers
        metric_a = [item['metric_a'] for item in self.sample_data]
        metric_b = [item['metric_b'] for item in self.sample_data]

        plt.figure(figsize=(8, 4))
        plt.plot(dates, metric_a, label='Metric A')
        plt.plot(dates, metric_b, label='Metric B')
        plt.title('Sample Report Data')
        plt.xlabel('Day of Month')
        plt.ylabel('Value')
        plt.legend()
        plt.tight_layout()

        # Save the graph to a temporary buffer
        buf = BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)
        plt.close()

        # Display the graph in Kivy
        self.ids.content_area.add_widget(Image(source=buf))

    def show_table(self):
        self.ids.content_area.clear_widgets()

        # Create a table layout
        table = GridLayout(cols=4, spacing=5, size_hint=(1, None), padding=10)
        table.bind(minimum_height=table.setter('height'))

        # Add headers with styling
        headers = ['Date', 'Metric A', 'Metric B', 'Metric C']
        for header in headers:
            lbl = Label(text=header, bold=True, color=(0, 0, 0, 1), size_hint_y=None, height=40)
            lbl.canvas.before.add(Color(0.8, 0.8, 0.8, 1))
            lbl.canvas.before.add(Rectangle(pos=lbl.pos, size=lbl.size))
            table.add_widget(lbl)

        # Add data rows with alternating colors
        for i, item in enumerate(self.sample_data):
            bg_color = (0.9, 0.9, 0.9, 1) if i % 2 == 0 else (1, 1, 1, 1)

            for key in ['date', 'metric_a', 'metric_b', 'metric_c']:
                lbl = Label(text=str(item[key]), size_hint_y=None, height=30)
                lbl.canvas.before.add(Color(*bg_color))
                lbl.canvas.before.add(Rectangle(pos=lbl.pos, size=lbl.size))
                table.add_widget(lbl)

        # Add scrolling capability
        scroll = ScrollView(size_hint=(1, 1))
        scroll.add_widget(table)
        self.ids.content_area.add_widget(scroll)

    def filtered_data(self):
        # In a real app, this would filter based on the selected month/dates
        return self.sample_data

    def show_popup(self, title, message):
        content = BoxLayout(orientation='vertical', padding=10, spacing=10)
        content.add_widget(Label(text=message))

        btn = Button(text='OK', size_hint=(1, None), height=40)
        popup = Popup(title=title, content=content, size_hint=(0.8, 0.4))
        btn.bind(on_press=popup.dismiss)
        content.add_widget(btn)

        popup.open()

class ReportDashboardApp(App):
    print("Hola")
    def build(self):
        self.title = "Report Dashboard"  # Set the window title
        return ReportDashboard()

if _name_ == '_main_':
    ReportDashboardApp().run()