import tkinter as tk
import os
import textwrap
from models import expenses, summary, predictions
from PIL import Image, ImageTk, ImageDraw

class Dashboard:
    def __init__(self, root):
        self.root = root
        self.root.title("Finance Tracker")
        self.root.geometry("400x500")
        self.root.configure(bg="#FFFC30")  # Lemon color

        self.create_top_frame()  # Create the top frame
        self.create_text_frame() # Create the text frame
        self.create_bottom_frame() # Create the bottom frame

    def create_top_frame(self):
        """Creates the top frame with title and buttons."""
        frame_top = tk.Frame(self.root, bg="#FFFC30")
        frame_top.pack(fill=tk.X, padx=10, pady=20)

        # Title label
        self.label = tk.Label(frame_top, text="Hi, Ivan", font=("Arial", 16, "bold"), bg="#FFFC30", fg="black")
        self.label.pack(side=tk.LEFT)

        # Power button
        power_icon = self.load_rounded_image("power.png", (10, 10), 10)
        if power_icon:
            self.btn_exit = tk.Button(frame_top, image=power_icon, command=self.root.quit, borderwidth=0, highlightbackground="#FFFC30")
            self.btn_exit.image = power_icon
            self.btn_exit.pack(side=tk.RIGHT, anchor="ne", padx=2)

        # Settings button
        settings_icon = self.load_rounded_image("settings.png", (10, 10), 10)
        if settings_icon:
            self.btn_settings = tk.Button(frame_top, image=settings_icon, command=self.open_settings, borderwidth=0)
            self.btn_settings.image = settings_icon
            self.btn_settings.pack(side=tk.RIGHT, anchor="ne", padx=2)

    def create_text_frame(self):
        """Creates the frame for the text display."""
        frame_text = tk.Frame(self.root, bg="#FFFFFF")
        frame_text.place(relx=0.5, rely=0.45, anchor=tk.CENTER, relwidth=0.9, relheight=0.5)


        # Text label in the internal frame
        lorem_text = (
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum vulputate lacus et nisl aliquet, et hendrerit arcu tincidunt. "
            "Donec non nibh eget tortor fringilla placerat. Curabitur ut aliquet urna, "
            "non scelerisque ipsum. Sed viverra ligula sit amet arcu scelerisque, "
            "ut feugiat felis luctus. Nam ultricies urna ut magna iaculis, at cursus "
            "risus rhoncus. Integer nec felis at velit convallis vehicula at at turpis."
        )

        # Ajustar el texto al ancho del frame (wrap width de 50 caracteres como estimación)
        wrapped_text = "\n".join(textwrap.wrap(lorem_text, width=50))

        # Crear un widget de texto en lugar de Label para mejor formato
        text_widget = tk.Text(frame_text, font=("Arial", 9), fg="#2d4340", bg="#FFFFFF", wrap="word")
        text_widget.insert("1.0", wrapped_text)
        text_widget.config(state="disabled", relief="flat")  # Deshabilitar edición
        text_widget.pack(expand=True, fill="both")
    def create_bottom_frame(self):
        """Creates the frame with the bottom buttons."""
        frame_buttons = tk.Frame(self.root, bg="#FFFC30")
        frame_buttons.place(relx=0.5, rely=0.8, anchor=tk.CENTER)

        # Expenses button
        expenses_icon = self.load_rounded_image("expenses.png", (60, 60), 15)
        if expenses_icon:
            self.btn_expenses = tk.Button(frame_buttons, image=expenses_icon, command=expenses.add_expense, borderwidth=0)
            self.btn_expenses.image = expenses_icon
            self.btn_expenses.grid(row=0, column=0, padx=5, pady=5)

        # Summary button
        summary_icon = self.load_rounded_image("summary.png", (60, 60), 15)
        if summary_icon:
            self.btn_summary = tk.Button(frame_buttons, image=summary_icon, command=summary.view_summary, borderwidth=0)
            self.btn_summary.image = summary_icon
            self.btn_summary.grid(row=0, column=1, padx=5, pady=5)

        # Predictions button
        predictions_icon = self.load_rounded_image("predictions.png", (60, 60), 15)
        if predictions_icon:
            self.btn_predictions = tk.Button(frame_buttons, image=predictions_icon, command=predictions.predict_expenses, borderwidth=0)
            self.btn_predictions.image = predictions_icon
            self.btn_predictions.grid(row=0, column=2, padx=5, pady=5)

    def load_rounded_image(self, image_name, size, radius):
        """Loads an image, applies rounded corners, and returns a PhotoImage object."""
        script_dir = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(script_dir, "..", "..", "static", "image", image_name)
        
        try:
            original_image = Image.open(image_path).convert("RGBA")
            resized_image = original_image.resize(size, Image.LANCZOS)

            # Create rounded mask
            mask = Image.new("L", size, 0)
            draw = ImageDraw.Draw(mask)
            draw.rounded_rectangle((0, 0, size[0], size[1]), radius, fill=255)

            # Apply mask to image
            rounded_image = Image.new("RGBA", size)
            rounded_image.paste(resized_image, (0, 0), mask)

            return ImageTk.PhotoImage(rounded_image)
        except FileNotFoundError:
            print(f"Image file not found at {image_path}")
            return None

    def open_settings(self):
        print("Open settings")

    def show(self):
        print("Displaying dashboard")

if __name__ == "__main__":
    root = tk.Tk()
    app = Dashboard(root)
    root.mainloop()
