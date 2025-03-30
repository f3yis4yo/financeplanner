import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle

class CustomGrid(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.rows = 5

        # Color de fondo
        with self.canvas.before:
            Color(1, 1, 0.188)  # Color #FFFC30 en RGB
            self.rect = Rectangle(size=self.size, pos=self.pos)

        self.bind(size=self._update_rect, pos=self._update_rect)

        # Fila A
        row_a = GridLayout(cols=9, size_hint_y=0.5)
        for i in range(7):
            row_a.add_widget(Label(text=''))
        row_a.add_widget(Button(text='A8'))
        row_a.add_widget(Button(text='A9'))
        self.add_widget(row_a)

        # Fila B
        row_b = GridLayout(cols=1)
        label_b = Label(text='Hi Ivan', halign='left', font_name='Arial', font_size=30, bold=True)
        row_b.add_widget(label_b)
        self.add_widget(row_b)

        # Fila C (doble altura)
        row_c = GridLayout(cols=1, size_hint_y=3)
        row_c.add_widget(Label(text='C'))
        self.add_widget(row_c)

        # Fila D
        row_d = GridLayout(cols=5)
        row_d.add_widget(Label(text=''))
        row_d.add_widget(Button(text='D2'))
        row_d.add_widget(Button(text='D3'))
        row_d.add_widget(Button(text='D4'))
        row_d.add_widget(Label(text=''))
        self.add_widget(row_d)

        # Fila E (año 2025 centrado)
        row_e = BoxLayout()
        row_e.add_widget(Label(text=''))  # Espacio a la izquierda
        row_e.add_widget(Label(text='2025'))  # Año centrado
        row_e.add_widget(Label(text=''))  # Espacio a la derecha
        row_e.children[1].halign = 'center'  # Centrar el año
        self.add_widget(row_e)

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

class MyApp(App):
    def build(self):
        return CustomGrid()

if __name__ == '__main__':
    MyApp().run()