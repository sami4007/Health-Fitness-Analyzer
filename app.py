import tkinter as tk
from tkinter import ttk

from dashboards.user_dashboard import UserDashboard
from dashboards.health_dashboard import HealthDashboard  


class Application:

    def __init__(self, root):

        self.root = root

        self.root.title("Health Fitness & Calorie Tracker")

        self.root.geometry("1200x800")

        self.root.resizable(False, False)

        self.root.configure(
            bg="#F5FAFD"
        )

        self.create_header()

        self.create_navigation()

        self.create_content_area()

        self.show_user_dashboard()

    # -------------------------------------

    def create_header(self):

        self.header = tk.Frame(
            self.root,
            bg="white"
        )

        self.header.pack(fill="x")

        tk.Label(
            self.header,
            text="🏃 Health Fitness & Calorie Tracker",
            font=("Segoe UI", 17, "bold"),
            bg="white",
            fg="#114B5F"
        ).pack(pady=(6, 0))

        tk.Label(
            self.header,
            text="Health & Nutrition Analysis System",
            font=("Segoe UI", 9),
            bg="white",
            fg="#666666"
        ).pack(pady=(0, 5))

    # -------------------------------------

    def create_navigation(self):

        self.nav = tk.Frame(
            self.root,
            bg="#114B5F"
        )
        self.nav.pack(fill="x")

        # Container for centering buttons
        button_frame = tk.Frame(
            self.nav,
            bg="#114B5F"
        )
        button_frame.pack()

        self.nav_buttons = []

        buttons = [
            ("👤 User", self.show_user_dashboard),
            ("📅 Health", self.show_daily_dashboard),
            ("🍎 Nutrition", self.show_nutrition_dashboard),
            ("📊 Analytics", self.show_analytics_dashboard)
        ]

        for text, command in buttons:

            btn = tk.Button(
                button_frame,
                text=text,
                command=command,
                bg="#114B5F",
                fg="white",
                activebackground="#1E6D84",
                activeforeground="white",
                bd=0,
                relief="flat",
                padx=18,
                pady=8,
                cursor="hand2",
                font=("Segoe UI", 10, "bold")
            )

            btn.pack(side="left", padx=8, pady=5)

            self.nav_buttons.append(btn)

    # -------------------------------------

    def create_content_area(self):

        self.content = tk.Frame(
            self.root,
            bg="#F5FAFD"
        )

        self.content.pack(fill="both", expand=True)

    # -------------------------------------

    def highlight_button(self, index):

        for i, btn in enumerate(self.nav_buttons):

            if i == index:
                btn.config(
                    bg="#1E6D84",
                    fg="white"
                )
            else:
                btn.config(
                    bg="#114B5F",
                    fg="white"
                )

    # -------------------------------------

    def clear_content(self):

        for widget in self.content.winfo_children():

            widget.destroy()

    # -------------------------------------

    def show_user_dashboard(self):

        self.highlight_button(0)

        self.clear_content()

        UserDashboard(self.content)

    # -------------------------------------

    def show_daily_dashboard(self):

        self.highlight_button(1)

        self.clear_content()

        
        HealthDashboard(self.content)

    # -------------------------------------

    def show_nutrition_dashboard(self):

        self.highlight_button(2)

        self.clear_content()

        ttk.Label(
            self.content,
            text="Dashboard 3 Coming Soon",
            font=("Segoe UI", 18)
        ).pack(expand=True)

    # -------------------------------------

    def show_analytics_dashboard(self):

        self.highlight_button(3)

        self.clear_content()

        ttk.Label(
            self.content,
            text="Dashboard 4 Coming Soon",
            font=("Segoe UI", 18)
        ).pack(expand=True)


if __name__ == "__main__":
    root = tk.Tk()
    app = Application(root)
    root.mainloop()