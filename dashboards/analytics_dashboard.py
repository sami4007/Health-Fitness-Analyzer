"""
Population Health Analytics Dashboard
"""

import tkinter as tk

from controllers.analytics_controller import AnalyticsController
from config import POPULATION_DATASET
from controllers.user_controller import UserController

class AnalyticsDashboard:

    def __init__(self, parent):

        self.root = parent
        self.controller = AnalyticsController()
        self.user_controller = UserController()

        self.root.configure(bg="#F5FAFD")

        self.create_widgets()

    # -------------------------------------------------

    def create_widgets(self):

        self.content_frame = tk.Frame(self.root, bg="#F5FAFD")

        self.content_frame.pack(fill="both", expand=True, padx=20, pady=15)

        self.create_top_section()
        self.create_summary_frame()
        self.create_bottom_section()

    # -------------------------------------------------

    def create_top_section(self):

        top = tk.Frame(self.content_frame, bg="#F5FAFD")

        top.pack(fill="x", pady=(0, 15))

        # ===============================
        # Dataset Information
        # ===============================

        dataset = tk.LabelFrame(
            top,
            text="📂 Dataset Information",
            font=("Segoe UI", 11, "bold"),
            bg="#F5FAFD",
            padx=15,
            pady=10,
        )

        dataset.pack(side="left", fill="x", expand=True, anchor="n")

        self.dataset_name = tk.Label(
            dataset,
            text=f"Dataset : {POPULATION_DATASET}",
            font=("Segoe UI", 10),
            bg="#F5FAFD",
            anchor="w",
        )

        self.dataset_name.pack(anchor="w", pady=4)

        self.rows_label = tk.Label(
            dataset, text="Rows : -", font=("Segoe UI", 10), bg="#F5FAFD", anchor="w"
        )

        self.rows_label.pack(anchor="w", pady=4)

        self.columns_label = tk.Label(
            dataset, text="Columns : -", font=("Segoe UI", 10), bg="#F5FAFD", anchor="w"
        )

        self.columns_label.pack(anchor="w", pady=4)

        # ===============================
        # Quick Actions
        # ===============================

        actions = tk.LabelFrame(
            top,
            text="⚡ Quick Actions",
            font=("Segoe UI", 11, "bold"),
            bg="#F5FAFD",
            padx=15,
            pady=10,
        )

        actions.pack(side="left", padx=(20, 0), fill="y")

        self.load_button = tk.Button(
            actions,
            text="📂 Load Dataset",
            width=18,
            font=("Segoe UI", 10, "bold"),
            cursor="hand2",
            command=self.load_dataset,
        )

        self.load_button.pack(pady=5)

        self.analyze_button = tk.Button(
            actions,
            text="📊 Analyze",
            width=18,
            font=("Segoe UI", 10, "bold"),
            cursor="hand2",
            command=self.analyze_dataset,
        )

        self.analyze_button.pack(pady=5)

        self.clear_button = tk.Button(
            actions,
            text="🧹 Clear",
            width=18,
            font=("Segoe UI", 10, "bold"),
            cursor="hand2",
            command=self.clear_dashboard,
        )

        self.clear_button.pack(pady=5)
    # -------------------------------------------------
    def create_summary_frame(self):

        summary_frame = tk.LabelFrame(
            self.content_frame,
            text="📊 Population Analytics",
            font=("Segoe UI", 11, "bold"),
            bg="#F5FAFD",
            padx=15,
            pady=15,
        )

        summary_frame.pack(fill="x", pady=(0, 10))

        # Configure two equal columns
        summary_frame.grid_columnconfigure(0, weight=1)
        summary_frame.grid_columnconfigure(1, weight=1)

        # ---------------- Average BMI ----------------
        tk.Label(
            summary_frame,
            text="Average BMI :",
            font=("Segoe UI", 11),
            bg="#F5FAFD",
        ).grid(row=0, column=0, sticky="w", padx=10, pady=8)

        self.avg_bmi_value = tk.Label(
            summary_frame,
            text="-",
            font=("Segoe UI", 13, "bold"),
            fg="#114B5F",
            bg="#F5FAFD",
        )

        self.avg_bmi_value.grid(row=0, column=0, sticky="e", padx=10)

        # ---------------- Healthy ----------------
        tk.Label(
            summary_frame,
            text="Healthy :",
            font=("Segoe UI", 11),
            bg="#F5FAFD",
        ).grid(row=0, column=1, sticky="w", padx=10, pady=8)

        self.healthy_value = tk.Label(
            summary_frame,
            text="-",
            font=("Segoe UI", 13, "bold"),
            fg="green",
            bg="#F5FAFD",
        )

        self.healthy_value.grid(row=0, column=1, sticky="e", padx=10)

        # ---------------- Overweight ----------------
        tk.Label(
            summary_frame,
            text="Overweight :",
            font=("Segoe UI", 11),
            bg="#F5FAFD",
        ).grid(row=1, column=0, sticky="w", padx=10, pady=8)

        self.overweight_value = tk.Label(
            summary_frame,
            text="-",
            font=("Segoe UI", 13, "bold"),
            fg="orange",
            bg="#F5FAFD",
        )

        self.overweight_value.grid(row=1, column=0, sticky="e", padx=10)

        # ---------------- Obese ----------------
        tk.Label(
            summary_frame,
            text="Obese :",
            font=("Segoe UI", 11),
            bg="#F5FAFD",
        ).grid(row=1, column=1, sticky="w", padx=10, pady=8)

        self.obese_value = tk.Label(
            summary_frame,
            text="-",
            font=("Segoe UI", 13, "bold"),
            fg="red",
            bg="#F5FAFD",
        )

        self.obese_value.grid(row=1, column=1, sticky="e", padx=10)

    def create_bottom_section(self):
        bottom_frame = tk.Frame(self.content_frame, bg="#F5FAFD")
        bottom_frame.pack(fill="both", expand=True, pady=(5, 0))

        # Make left and right take equal width
        bottom_frame.grid_columnconfigure(0, weight=1)
        bottom_frame.grid_columnconfigure(1, weight=1)
        bottom_frame.grid_rowconfigure(0, weight=1)

        # ===================================================
        # User Analytics
        # ===================================================

        user_frame = tk.LabelFrame(
            bottom_frame,
            text="📊 User Analytics",
            font=("Segoe UI", 11, "bold"),
            bg="#F5FAFD",
            padx=15,
            pady=15,
        )

        user_frame.grid(row=0, column=0, sticky="nsew", padx=(0, 10))

        user_frame.grid_columnconfigure(0, weight=1)
        user_frame.grid_columnconfigure(1, weight=1)

        tk.Label(
            user_frame,
            text="Average BMI :",
            font=("Segoe UI", 11),
            bg="#F5FAFD",
        ).grid(row=0, column=0, sticky="w", pady=8)

        self.user_avg_bmi = tk.Label(
            user_frame,
            text="-",
            font=("Segoe UI", 13, "bold"),
            fg="#114B5F",
            bg="#F5FAFD",
        )
        self.user_avg_bmi.grid(row=0, column=1, sticky="e")

        tk.Label(
            user_frame,
            text="Healthy :",
            font=("Segoe UI", 11),
            bg="#F5FAFD",
        ).grid(row=1, column=0, sticky="w", pady=8)

        self.user_healthy = tk.Label(
            user_frame,
            text="-",
            font=("Segoe UI", 13, "bold"),
            fg="green",
            bg="#F5FAFD",
        )
        self.user_healthy.grid(row=1, column=1, sticky="e")

        tk.Label(
            user_frame,
            text="Overweight :",
            font=("Segoe UI", 11),
            bg="#F5FAFD",
        ).grid(row=2, column=0, sticky="w", pady=8)

        self.user_overweight = tk.Label(
            user_frame,
            text="-",
            font=("Segoe UI", 13, "bold"),
            fg="orange",
            bg="#F5FAFD",
        )
        self.user_overweight.grid(row=2, column=1, sticky="e")

        tk.Label(
            user_frame,
            text="Obese :",
            font=("Segoe UI", 11),
            bg="#F5FAFD",
        ).grid(row=3, column=0, sticky="w", pady=8)

        self.user_obese = tk.Label(
            user_frame,
            text="-",
            font=("Segoe UI", 13, "bold"),
            fg="red",
            bg="#F5FAFD",
        )
        self.user_obese.grid(row=3, column=1, sticky="e")

        button_frame = tk.Frame(user_frame, bg="#F5FAFD")
        button_frame.grid(row=4, column=0, columnspan=2, pady=20)

        tk.Button(
            button_frame,
            text="📊 Analyze User",
            width=15,
            command=self.analyze_user,
        ).pack(side="left", padx=5)

        tk.Button(
            button_frame,
            text="🧹 Clear User",
            width=15,
            command=self.clear_user,
        ).pack(side="left", padx=5)

        # ===================================================
        # Bar Chart
        # ===================================================

        self.chart_frame = tk.LabelFrame(
            bottom_frame,
            text="📈 Population & User Bar Chart",
            font=("Segoe UI", 11, "bold"),
            bg="#F5FAFD",
            padx=15,
            pady=15,
        )

        self.chart_frame.grid(row=0, column=1, sticky="nsew")

        self.chart_canvas = tk.Canvas(
    self.chart_frame,
    bg="white",
    highlightthickness=1,
    highlightbackground="#CFCFCF"
)

        self.chart_canvas.pack(
    fill="both",
    expand=True,
    padx=10,
    pady=10
        )

    # -------------------------------------------------
    # Button Methods
    # -------------------------------------------------

    def load_dataset(self):

        rows, columns = self.controller.load_dataset()

        self.dataset_name.config(text="Dataset : enhanced_health_data.csv")

        self.rows_label.config(text=f"Rows : {rows}")

        self.columns_label.config(text=f"Columns : {columns}")

    def analyze_dataset(self):

        results = self.controller.analyze_dataset()

        self.avg_bmi_value.config(text=str(results["average_bmi"]))

        self.healthy_value.config(text=str(results["healthy"]))

        self.overweight_value.config(text=str(results["overweight"]))

        self.obese_value.config(text=str(results["obese"]))

        self.draw_population_chart(
          results["healthy"],
          results["overweight"],
          results["obese"]
             )

    def analyze_user(self):

        results = self.user_controller.analyze_users()

        self.user_avg_bmi.config(text=str(results["average_bmi"]))

        self.user_healthy.config(text=str(results["healthy"]))

        self.user_overweight.config(text=str(results["overweight"]))

        self.user_obese.config(text=str(results["obese"]))

        self.draw_population_chart(results["healthy"], results["overweight"], results["obese"])

    def draw_population_chart(self, healthy, overweight, obese):
        # Clear previous chart
        self.chart_canvas.delete("all")
        # Calculate bar widths
        max_value = max(healthy, overweight, obese) if max(healthy, overweight, obese) > 0 else 1

        healthy_width = (healthy / max_value) * 200
        overweight_width = (overweight / max_value) * 200
        obese_width = (obese / max_value) * 200

        # Title
        self.chart_canvas.create_text(
            180,
            20,
            text="Population BMI Distribution",
            font=("Segoe UI", 12, "bold")
        )

        # Healthy
        self.chart_canvas.create_text(
            20, 60,
            text="Healthy",
            anchor="w",
            font=("Segoe UI", 10)
        )

        self.chart_canvas.create_rectangle(
            100, 50,
            100 + healthy_width, 75,
            fill="green"
        )

        # Overweight
        self.chart_canvas.create_text(
            20, 110,
            text="Overweight",
            anchor="w",
            font=("Segoe UI", 10)
        )

        self.chart_canvas.create_rectangle(
            100, 100,
            100 + overweight_width, 125,
            fill="orange"
        )

        # Obese
        self.chart_canvas.create_text(
            20, 160,
            text="Obese",
            anchor="w",
            font=("Segoe UI", 10)
        )

        self.chart_canvas.create_rectangle(
            100, 150,
            100 + obese_width, 175,
            fill="red"
        )

    def clear_user(self):
        self.user_avg_bmi.config(text="-")
        self.user_healthy.config(text="-")
        self.user_overweight.config(text="-")
        self.user_obese.config(text="-")
        self.chart_canvas.delete("all")

    def clear_dashboard(self):

        self.dataset_name.config(text=f"Dataset : {POPULATION_DATASET}")

        self.rows_label.config(text="Rows : -")
        self.columns_label.config(text="Columns : -")

        self.avg_bmi_value.config(text="-")
        self.healthy_value.config(text="-")
        self.overweight_value.config(text="-")
        self.obese_value.config(text="-")
        self.chart_canvas.delete("all")
