import tkinter as tk
from tkinter import messagebox
from controllers.health_controller import UserController

class HealthDashboard(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="#F5FAFD")
        self.pack(fill="both", expand=True)

        self.controller = UserController()

        # Heading
        heading_label = tk.Label(self, text="Health Analysis Dashboard", font=("Arial", 22, "bold"), bg="#F5FAFD")
        heading_label.pack(padx=30, pady=10)

        # Inner Frame
        self.frame = tk.Frame(self, bg="#F5FAFD")
        self.frame.pack(fill="x", padx=20, pady=10)
        self.frame.columnconfigure(0, weight=1)
        self.frame.columnconfigure(1, weight=1)

        self.create_personal_info_frame()
        self.create_result_info_frame()
        self.create_recommendation_frame()

    def create_personal_info_frame(self):
        personal_info_frame = tk.LabelFrame(self.frame, text="Personal Information", padx=15, pady=15)
        personal_info_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        personal_info_frame.columnconfigure(1, weight=1)

        tk.Label(personal_info_frame, text="Name  ").grid(row=0, column=0, sticky="w")
        self.Name_entry = tk.Entry(personal_info_frame)
        self.Name_entry.grid(row=0, column=1, sticky="ew", pady=2)

        tk.Label(personal_info_frame, text="Gender(Male/Female) ").grid(row=1, column=0, sticky="w")
        self.Gender_entry = tk.Entry(personal_info_frame)
        self.Gender_entry.grid(row=1, column=1, sticky="ew", pady=2)

        tk.Label(personal_info_frame, text="Age  ").grid(row=2, column=0, sticky="w")
        self.Age_entry = tk.Entry(personal_info_frame)
        self.Age_entry.grid(row=2, column=1, sticky="ew", pady=2)

        tk.Label(personal_info_frame, text="Height (cm) ").grid(row=3, column=0, sticky="w")
        self.Height_entry = tk.Entry(personal_info_frame)
        self.Height_entry.grid(row=3, column=1, sticky="ew", pady=2)

        tk.Label(personal_info_frame, text="Weight (kg)  ").grid(row=4, column=0, sticky="w")
        self.Weight_entry = tk.Entry(personal_info_frame)
        self.Weight_entry.grid(row=4, column=1, sticky="ew", pady=2)

        tk.Label(personal_info_frame, text="Calories  ").grid(row=5, column=0, sticky="w")
        self.Calories_entry = tk.Entry(personal_info_frame)
        self.Calories_entry.grid(row=5, column=1, sticky="ew", pady=2)

        tk.Label(personal_info_frame, text="Excercise (hr) ").grid(row=6, column=0, sticky="w")
        self.Excercise_entry = tk.Entry(personal_info_frame)
        self.Excercise_entry.grid(row=6, column=1, sticky="ew", pady=2)

        tk.Label(personal_info_frame, text="Water Intake (L) ").grid(row=7, column=0, sticky="w")
        self.Water_Intake_entry = tk.Entry(personal_info_frame)
        self.Water_Intake_entry.grid(row=7, column=1, sticky="ew", pady=2)

        # Buttons
        Calculate_button = tk.Button(personal_info_frame, text="Calculate", command=self.calculate, width=12, bg="#4CAF50", fg="white")
        Calculate_button.grid(row=8, column=0, pady=15)

        Clear_button = tk.Button(personal_info_frame, text="Clear", command=self.clear, width=12, bg="#E53935", fg="white")
        Clear_button.grid(row=8, column=1, pady=15)

    def create_result_info_frame(self):
        Result_info_frame = tk.LabelFrame(self.frame, text="Result", padx=15, pady=15)
        Result_info_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
        Result_info_frame.columnconfigure(1, weight=1)

        tk.Label(Result_info_frame, text="BMI  ").grid(row=0, column=0, sticky="w")
        self.BMI_entry = tk.Entry(Result_info_frame)
        self.BMI_entry.grid(row=0, column=1, sticky="ew", pady=2)

        tk.Label(Result_info_frame, text="Status  ").grid(row=1, column=0, sticky="w")
        self.Status_entry = tk.Entry(Result_info_frame)
        self.Status_entry.grid(row=1, column=1, sticky="ew", pady=2)

        tk.Label(Result_info_frame, text="Body Fat").grid(row=2, column=0, sticky="w")
        self.Body_fat_entry = tk.Entry(Result_info_frame)
        self.Body_fat_entry.grid(row=2, column=1, sticky="ew", pady=2)

        tk.Label(Result_info_frame, text="Water Need").grid(row=3, column=0, sticky="w")
        self.Water_need_entry = tk.Entry(Result_info_frame)
        self.Water_need_entry.grid(row=3, column=1, sticky="ew", pady=2)

        tk.Label(Result_info_frame, text="Ideal Weight").grid(row=4, column=0, sticky="w")
        self.Ideal_weight_entry = tk.Entry(Result_info_frame)
        self.Ideal_weight_entry.grid(row=4, column=1, sticky="ew", pady=2)

        tk.Label(Result_info_frame, text="Recommended Calories").grid(row=5, column=0, sticky="w")
        self.Recommended_calories_entry = tk.Entry(Result_info_frame)
        self.Recommended_calories_entry.grid(row=5, column=1, sticky="ew", pady=2)

        tk.Label(Result_info_frame, text="Health Score").grid(row=6, column=0, sticky="w")
        self.Health_score_entry = tk.Entry(Result_info_frame)
        self.Health_score_entry.grid(row=6, column=1, sticky="ew", pady=2)

    def create_recommendation_frame(self):
        recommendation_frame = tk.LabelFrame(self, text="Recommendation", padx=15, pady=10)
        recommendation_frame.pack(padx=30, pady=10, fill="x")

        self.recommendation_text = tk.Text(recommendation_frame, height=8, font=("Arial", 11), wrap="word")
        self.recommendation_text.pack(fill="x", padx=5, pady=5)

    def calculate(self):
        try:
            name = self.Name_entry.get().strip()
            gender = self.Gender_entry.get().strip()
            height = float(self.Height_entry.get())
            weight = float(self.Weight_entry.get())
            age = int(self.Age_entry.get())
            calories = int(self.Calories_entry.get())
            exercise = float(self.Excercise_entry.get())
            water = float(self.Water_Intake_entry.get())

            if not name:
                messagebox.showerror("Input Error", "Please enter a Name!")
                return

            user, rec_message = self.controller.add_user(
                name, gender, age, height, weight, calories, exercise, water
            )

            self.clear_outputs()

            self.BMI_entry.insert(0, f"{user.bmi:.2f}")
            self.Status_entry.insert(0, user.status)
            self.Body_fat_entry.insert(0, f"{user.body_fat:.2f}%")
            self.Water_need_entry.insert(0, f"{user.water_need:.2f} L")
            self.Ideal_weight_entry.insert(0, f"{user.ideal_weight:.2f} kg")
            self.Recommended_calories_entry.insert(0, f"{user.recommended_calories} kcal")
            self.Health_score_entry.insert(0, str(user.health_score))

            self.recommendation_text.insert(tk.END, rec_message)

        except ValueError:
            messagebox.showerror("Input Error", "Please fill in all fields correctly !")

    def clear_outputs(self):
        self.BMI_entry.delete(0, tk.END)
        self.Status_entry.delete(0, tk.END)
        self.Body_fat_entry.delete(0, tk.END)
        self.Water_need_entry.delete(0, tk.END)
        self.Ideal_weight_entry.delete(0, tk.END)
        self.Recommended_calories_entry.delete(0, tk.END)
        self.Health_score_entry.delete(0, tk.END)
        self.recommendation_text.delete("1.0", tk.END)

    def clear(self):
        self.Name_entry.delete(0, tk.END)
        self.Gender_entry.delete(0, tk.END)
        self.Age_entry.delete(0, tk.END)
        self.Height_entry.delete(0, tk.END)
        self.Weight_entry.delete(0, tk.END)
        self.Calories_entry.delete(0, tk.END)
        self.Excercise_entry.delete(0, tk.END)
        self.Water_Intake_entry.delete(0, tk.END)

        self.clear_outputs()