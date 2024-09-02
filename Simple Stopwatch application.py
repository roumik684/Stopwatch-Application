import tkinter as tk
from datetime import datetime
import time
import random

class StopwatchApp:
    def __init__(self, root):
        self.root = root
        self.root.title(" Stopwatch Application")

        # Stopwatch variables
        self.start_time = 0
        self.elapsed_time = 0
        self.running = False

        # UI Setup
        self.setup_ui()

    def setup_ui(self):
        # Date label
        self.date_label = tk.Label(self.root, text="", font=("Helvetica", 16))
        self.date_label.pack(pady=10)

        # Time label
        self.time_label = tk.Label(self.root, text="00:00:00", font=("Helvetica", 36))
        self.time_label.pack(pady=20)

        # Buttons
        button_frame = tk.Frame(self.root)
        button_frame.pack()

        self.start_button = tk.Button(button_frame, text="Start", command=self.start, width=10)
        self.start_button.grid(row=0, column=0, padx=5)

        self.stop_button = tk.Button(button_frame, text="Stop", command=self.stop, width=10)
        self.stop_button.grid(row=0, column=1, padx=5)

        self.reset_button = tk.Button(button_frame, text="Reset", command=self.reset, width=10)
        self.reset_button.grid(row=0, column=2, padx=5)

        # Update UI
        self.update_ui()

    def start(self):
        if not self.running:
            self.start_time = time.time() - self.elapsed_time
            self.running = True
            self.update_ui()

    def stop(self):
        if self.running:
            self.elapsed_time = time.time() - self.start_time
            self.running = False

    def reset(self):
        self.start_time = 0
        self.elapsed_time = 0
        self.time_label.config(text="00:00:00")
        self.running = False

    def update_ui(self):
        # Update the time display
        if self.running:
            self.elapsed_time = time.time() - self.start_time
            self.time_label.config(text=self.format_time(self.elapsed_time))

        # Update the date display
        self.date_label.config(text=self.current_date())

        # Update the background color
        self.root.config(bg=self.random_color())

        # Schedule next update
        self.root.after(1000, self.update_ui)

    def format_time(self, elapsed_time):
        hours = int(elapsed_time // 3600)
        minutes = int((elapsed_time % 3600) // 60)
        seconds = int(elapsed_time % 60)
        return f"{hours:02}:{minutes:02}:{seconds:02}"

    def current_date(self):
        return datetime.now().strftime("%Y-%m-%d")

    def random_color(self):
        colors = ["#FFB6C1", "#FF69B4", "#FF1493", "#DB7093", "#C71585", "#800080", "#8A2BE2", "#4B0082"]
        return random.choice(colors)

# Main Application
if __name__ == "__main__":
    root = tk.Tk()
    app = StopwatchApp(root)
    root.mainloop()
