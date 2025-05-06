from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle
from kivy.uix.image import Image
import matplotlib.pyplot as plt
from io import BytesIO
from datetime import datetime
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
from kivy.uix.textinput import TextInput

class ReportDashboard(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.spacing = 10
        self.padding = 10
        self.sample_data = self.generate_sample_data()
        self.build_ui()

    def build_ui(self):
        """Build the UI components programmatically"""
        # Filter controls
        filter_layout = BoxLayout(size_hint=(1, None), height=50)
        
        self.month_spinner = Spinner(
            text='Select Month',
            values=('January', 'February', 'March', 'April', 'May', 'June',
                    'July', 'August', 'September', 'October', 'November', 'December')
        )
        
        self.from_date = TextInput(hint_text='From (DD/MM/YYYY)', multiline=False)
        self.to_date = TextInput(hint_text='To (DD/MM/YYYY)', multiline=False)
        
        apply_btn = Button(text='Apply Filters', size_hint=(None, None), size=(120, 50))
        apply_btn.bind(on_press=lambda x: self.apply_filters())
        
        filter_layout.add_widget(self.month_spinner)
        filter_layout.add_widget(self.from_date)
        filter_layout.add_widget(self.to_date)
        filter_layout.add_widget(apply_btn)
        
        # Action buttons
        action_layout = BoxLayout(size_hint=(1, None), height=50)
        graph_btn = Button(text='Show Graph')
        table_btn = Button(text='Show Table')
        download_btn = Button(text='Download Report')
        
        graph_btn.bind(on_press=lambda x: self.show_graph())
        table_btn.bind(on_press=lambda x: self.show_table())
        download_btn.bind(on_press=lambda x: self.download_report())
        
        action_layout.add_widget(graph_btn)
        action_layout.add_widget(table_btn)
        action_layout.add_widget(download_btn)
        
        # Content area
        self.content_area = BoxLayout(orientation='vertical', size_hint=(1, 1))
        
        # Add all to main layout
        self.add_widget(filter_layout)
        self.add_widget(action_layout)
        self.add_widget(self.content_area)

    # ... (keep all existing methods unchanged from your original file) ...