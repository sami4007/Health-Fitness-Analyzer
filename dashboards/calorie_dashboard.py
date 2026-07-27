import tkinter as tk

from tkinter import ttk
from tkinter import messagebox

from datetime import datetime, timedelta

from controllers.calorie_controller import CalorieController


class CalorieDashboard:

    def __init__(self, root):

        self.root = root

        self.controller = CalorieController()

        self.create_variables()

        self.create_widgets()

        self.load_users()

        self.load_foods()

    # -------------------------------------------------

    def create_variables(self):

        self.user_id = tk.StringVar()

        self.date = tk.StringVar(
            value=datetime.today().strftime("%Y-%m-%d")
        )

        self.meal = tk.StringVar(
            value="Breakfast"
        )

        self.food_name = tk.StringVar()

        self.servings = tk.StringVar(
            value="1"
        )

        self.water = tk.StringVar(
            value="0"
        )

        self.calories_burned = tk.StringVar(
            value="0"
        )

        self.search_food = tk.StringVar()

    # -------------------------------------------------

    def create_widgets(self):

        self.content_frame = tk.Frame(

            self.root,

            bg="#F5FAFD"

        )
        self.content_frame.columnconfigure(
         1,
          weight=2
         )

        self.content_frame.pack(

            fill="both",

            expand=True,

            padx=20,

            pady=(10, 15)

        )

        self.content_frame.columnconfigure(
            0,
            weight=3
        )

        self.content_frame.columnconfigure(
            1,
            weight=2
        )

        self.content_frame.rowconfigure(2, weight=1)

        self.create_meal_frame()

        self.create_summary_cards()

        self.create_food_search_frame()

        self.create_daily_summary_frame()

        self.create_weekly_summary_frame()

        self.create_meal_table()

        # -------------------------------------------------

    def create_meal_frame(self):

        frame = ttk.LabelFrame(

            self.content_frame,

            text="🍽 Meal Entry",

            padding=15

        )

        frame.grid(

            row=0,

            column=0,

            sticky="nsew",

            padx=(0, 10),

            pady=(0, 10)

        )

        frame.columnconfigure(1, weight=1)
        frame.columnconfigure(3, weight=1)

        ttk.Label(
            frame,
            text="User ID"
        ).grid(
            row=0,
            column=0,
            padx=5,
            pady=8,
            sticky="w"
        )

        self.user_combobox = ttk.Combobox(

           frame,

           textvariable=self.user_id,

             state="readonly"

        )

        self.user_combobox.grid(

         row=0,

         column=1,

         sticky="ew",

          padx=5
 
     )



        self.user_combobox.bind(
    "<<ComboboxSelected>>",
    lambda event: self.refresh_dashboard()
)

        self.user_combobox.bind(
    "<<ComboboxSelected>>",
    self.user_changed
)

        ttk.Label(
            frame,
            text="Date"
        ).grid(
            row=0,
            column=2,
            padx=5,
            pady=8,
            sticky="w"
        )

        ttk.Entry(
            frame,
            textvariable=self.date
        ).grid(
            row=0,
            column=3,
            sticky="ew",
            padx=5
        )

        ttk.Label(
            frame,
            text="Meal"
        ).grid(
            row=1,
            column=0,
            padx=5,
            pady=8,
            sticky="w"
        )

        ttk.Combobox(

            frame,

            textvariable=self.meal,

            state="readonly",

            values=[
                "Breakfast",
                "Lunch",
                "Dinner",
                "Snacks"
            ]

        ).grid(

            row=1,

            column=1,

            sticky="ew",

            padx=5

        )

        ttk.Label(
            frame,
            text="Food"
        ).grid(
            row=1,
            column=2,
            padx=5,
            pady=8,
            sticky="w"
        )

        self.food_combobox = ttk.Combobox(

            frame,

            textvariable=self.food_name,

            state="readonly"

)

        self.food_combobox.grid(

            row=1,

            column=3,

            sticky="ew",

            padx=5

)

        self.food_combobox.bind(
    "<<ComboboxSelected>>",
    self.food_changed
)


        ttk.Label(
            frame,
            text="Quantity (100 g)"
        ).grid(
            row=2,
            column=0,
            padx=5,
            pady=8,
            sticky="w"
        )

        ttk.Entry(
            frame,
            textvariable=self.servings
        ).grid(
            row=2,
            column=1,
            sticky="ew",
            padx=5
        )

        ttk.Label(
            frame,
            text="Water (ml)"
        ).grid(
            row=2,
            column=2,
            padx=5,
            pady=8,
            sticky="w"
        )

        ttk.Entry(
            frame,
            textvariable=self.water
        ).grid(
            row=2,
            column=3,
            sticky="ew",
            padx=5
        )

        ttk.Label(
            frame,
            text="Calories Burned"
        ).grid(
            row=3,
            column=0,
            padx=5,
            pady=8,
            sticky="w"
        )

        ttk.Entry(
            frame,
            textvariable=self.calories_burned
        ).grid(
            row=3,
            column=1,
            sticky="ew",
            padx=5
        )

        button_frame = ttk.Frame(
            frame
        )

        button_frame.grid(

            row=4,

            column=0,

            columnspan=4,

            pady=(12, 0)

        )

        ttk.Button(

            button_frame,

            text="➕ Add Meal",

            command=self.add_meal,

            width=18

        ).pack(
            side="left",
            padx=5
        )

        ttk.Button(

            button_frame,

            text="💧 Save Water",

            command=self.save_water,

            width=18

        ).pack(
            side="left",
            padx=5
        )

        ttk.Button(

            button_frame,

            text="🔥 Save Burned",

            command=self.save_calories_burned,

            width=18

        ).pack(
            side="left",
            padx=5
        )

        ttk.Button(

            button_frame,

            text="🧹 Clear",

            command=self.clear_fields,

            width=18

        ).pack(
            side="left",
            padx=5
        )

    # -------------------------------------------------

    def create_summary_cards(self):

        frame = tk.Frame(

            self.content_frame,

            bg="#F5FAFD"

        )

        frame.grid(

            row=0,

            column=1,

            sticky="nsew",

            pady=(0, 10)

        )

        for i in range(4):

            frame.columnconfigure(
                i,
                weight=1
            )

        self.calories_value, _ = self.create_stat_card(

            frame,

            0,

            "🔥",

            "Calories",

            "0",

            ""

        )

        self.remaining_value, _ = self.create_stat_card(

            frame,

            1,

            "🎯",

            "Remaining",

            "0",

            ""

        )

        self.water_value, _ = self.create_stat_card(

            frame,

            2,

            "💧",

            "Water",

            "0",

            "ml"

        )

        self.burned_value, _ = self.create_stat_card(

            frame,

            3,

            "🏃",

            "Burned",

            "0",

            "kcal"

        )

    # -------------------------------------------------

    def create_stat_card(
        self,
        parent,
        column,
        icon,
        title,
        value,
        subtitle
    ):

        card = tk.Frame(

            parent,

            bg="white",

            bd=1,

            relief="solid"

        )

        card.grid(

            row=0,

            column=column,

            padx=5,

            sticky="nsew"

        )

        tk.Label(

            card,

            text=icon,

            font=("Segoe UI Emoji", 20),

            bg="white",

            fg="#1976D2"

        ).pack(
            pady=(6, 0)
        )

        tk.Label(

            card,

            text=title,

            bg="white",

            font=("Segoe UI", 10)

        ).pack()

        value_label = tk.Label(

            card,

            text=value,

            bg="white",

            fg="#114B5F",

            font=("Segoe UI", 18, "bold")

        )

        value_label.pack(
            pady=(2, 0)
        )

        subtitle_label = tk.Label(

            card,

            text=subtitle,

            bg="white",

            fg="#777777",

            font=("Segoe UI", 9)

        )

        subtitle_label.pack(
            pady=(0, 6)
        )

        return value_label, subtitle_label

    # -------------------------------------------------

    def create_food_search_frame(self):

        frame = ttk.LabelFrame(

            self.content_frame,

            text="🔍 Food Search",

            padding=15

        )

        frame.grid(

            row=1,

            column=0,

            sticky="ew",

            padx=(0, 10),

            pady=(0, 10)

        )

        frame.columnconfigure(
            1,
            weight=1
        )

        ttk.Label(

            frame,

            text="Food Name"

        ).grid(

            row=0,

            column=0,

            padx=5,

            pady=5,

            sticky="w"

        )

        ttk.Entry(

            frame,

            textvariable=self.search_food

        ).grid(

            row=0,

            column=1,

            sticky="ew",

            padx=5

        )

        ttk.Button(

            frame,

            text="Search",

            command=self.search_food_item

        ).grid(

            row=0,

            column=2,

            padx=5

        )

    # -------------------------------------------------

    def create_daily_summary_frame(self):

        frame = ttk.LabelFrame(

            self.content_frame,

            text="📋 Daily Summary",

            padding=15

        )

        frame.grid(

            row=1,

            column=1,

            sticky="nsew",

            pady=(0, 10)

        )

        self.daily_summary_text = tk.Text(

            frame,

            height=7,

            width=40,

            state="disabled",

            wrap="word"

        )

        self.daily_summary_text.pack(

            fill="both",

            expand=True

        )

    # -------------------------------------------------

    def create_weekly_summary_frame(self):

        frame = ttk.LabelFrame(

            self.content_frame,

            text="📈 Weekly Summary",

            padding=15

        )

        frame.grid(

            row=2,

            column=1,

            sticky="nsew",

            pady=(0, 10)

        )

        self.weekly_summary_text = tk.Text(

            frame,

            height=10,

            width=36,

            state="disabled",

            wrap="word"

        )

        self.weekly_summary_text.pack(

            fill="both",

            expand=True

        )

    # -------------------------------------------------

    def create_meal_table(self):

        frame = ttk.LabelFrame(

            self.content_frame,

            text="🍽 Today's Meals",

            padding=10

        )

        frame.grid(

            row=2,

            column=0,

            sticky="nsew",

            padx=(0, 10),

            pady=(0, 10)

        )

        frame.columnconfigure(
            0,
            weight=1
        )

        frame.rowconfigure(
            0,
            weight=1
        )

        columns = (

         "Meal",

         "Food",

         "Quantity (100 g)"

)

        self.tree = ttk.Treeview(

         frame,

               columns=columns,

               show="headings",

              height=11

                  )

        for column in columns:

            self.tree.heading(

                column,

                text=column

            )

            self.tree.column(
                "Meal",
                width=150,
                anchor="center"
)

            self.tree.column(
                "Food",
                width=220,
                anchor="center"
)

            self.tree.column(
                "Quantity (100 g)",
                 width=180,
                 anchor="center"
)

        scrollbar = ttk.Scrollbar(

            frame,

            orient="vertical",

            command=self.tree.yview

        )

        self.tree.configure(

            yscrollcommand=scrollbar.set

        )

        self.tree.grid(

            row=0,

            column=0,

            sticky="nsew"

        )

        scrollbar.grid(

            row=0,

            column=1,

            sticky="ns"

        )

        self.tree.tag_configure(

            "even",

            background="#F8FBFD"

        )

        self.tree.tag_configure(

            "odd",

            background="white"

        )

        self.tree.bind(

            "<Double-1>",

            self.select_meal

        )

        # -------------------------------------------------

    def add_meal(self):

        if (
            self.get_selected_user_id() == "" or
            self.food_name.get() == "" or
            self.servings.get() == ""
        ):

            messagebox.showwarning(
                "Warning",
                "Please complete all required fields."
            )

            return

        try:

            self.controller.add_meal(

                self.get_selected_user_id(),

                self.date.get(),

                self.meal.get(),

                self.food_name.get(),

                float(self.servings.get())

            )

            messagebox.showinfo(

                "Success",

                "Meal added successfully."

            )

            self.refresh_table()

            self.refresh_dashboard()

        except ValueError:

            messagebox.showerror(

                "Error",

                "Servings must be numeric."

            )

    # -------------------------------------------------

    def save_water(self):

        try:

            self.controller.update_water_intake(

                self.get_selected_user_id(),

                self.date.get(),

                float(self.water.get())

            )

            self.refresh_dashboard()

            messagebox.showinfo(

                "Success",

                "Water intake saved."

            )

        except ValueError:

            messagebox.showerror(

                "Error",

                "Invalid water value."

            )

    # -------------------------------------------------

    def save_calories_burned(self):

        try:

            self.controller.update_calories_burned(

                self.get_selected_user_id(),

                self.date.get(),

                float(self.calories_burned.get())

            )

            self.refresh_dashboard()

            messagebox.showinfo(

                "Success",

                "Calories burned updated."

            )

        except ValueError:

            messagebox.showerror(

                "Error",

                "Invalid calorie value."

            )

    # -------------------------------------------------

    def search_food_item(self):

        foods = self.controller.search_food(

            self.search_food.get()

        )

        if not foods:

            messagebox.showinfo(

                "Search",

                "No matching food found."

            )

            return

        result = ""

        for food in foods:

            result += (

                f"{food.food_name}\n"
                f"(Per 100 g)\n\n"

                f"Calories : {food.calories}\n"

                f"Protein : {food.protein} g\n"

                f"Carbs : {food.carbs} g\n"

                f"Fat : {food.fat} g\n\n"

            )

        messagebox.showinfo(

            "Food Search",

            result

        )

    # -------------------------------------------------

    def refresh_table(self):

     for item in self.tree.get_children():

        self.tree.delete(item)

     records = self.controller.get_daily_records(

        self.get_selected_user_id(),

        self.date.get()

    )
     print("UI User ID :", repr(self.get_selected_user_id()))
     print("UI Date    :", repr(self.date.get()))
     print("Records    :", len(records))

     for index, record in enumerate(records):

        print(
    record.user_id,
    record.date,
    record.food_name,
    record.servings
 )
      

        tag = "even" if index % 2 == 0 else "odd"

        self.tree.insert(

            "",

            "end",

            values=(

                record.meal,

                record.food_name,

                record.servings

            ),

            tags=(tag,)

        )

    # -------------------------------------------------

    def load_users(self):

        user_list = []

        for user in self.controller.users:

            user_list.append(
            f"{user.user_id} - {user.name}"
        )

        self.user_combobox["values"] = user_list

        if user_list:

         self.user_combobox.current(0)


    def load_foods(self):

        food_list = []

        for food in self.controller.food_database:

         food_list.append(
            food.food_name
        )

        self.food_combobox["values"] = food_list

        print(self.food_combobox["values"])

        if food_list:

         self.food_combobox.current(0)
       
    def get_selected_user_id(self):

        selected = self.user_id.get()

        if " - " in selected:

          return selected.split(" - ")[0]

        return selected

    def user_changed(self, event):

       self.refresh_dashboard()

       self.refresh_table()

    def food_changed(self, event):

        self.food_name.set(
           self.food_combobox.get()
    )
        
    def refresh_dashboard(self):

        if self.get_selected_user_id() == "":

            return

        summary = self.controller.daily_summary_report(

            self.get_selected_user_id(),

            self.date.get()

        ) 

        if summary is None:

            return

        self.calories_value.config(

            text=str(summary["consumed_calories"])

        )

        self.remaining_value.config(

            text=str(summary["remaining_calories"])

        )

        self.water_value.config(

            text=str(summary["water"])

        )

        self.burned_value.config(

            text=str(summary["calories_burned"])

        )

        self.generate_daily_summary()
        self.generate_weekly_summary()

    # -------------------------------------------------

    def generate_daily_summary(self):

        summary = self.controller.daily_summary_report(

            self.get_selected_user_id(),

            self.date.get()

        )

        if summary is None:

            return

        self.daily_summary_text.config(

            state="normal"

        )

        self.daily_summary_text.delete(

            "1.0",

            tk.END

        )

        text = (

            f"Daily Target : {summary['target_calories']} kcal\n\n"

            f"Calories Consumed : {summary['consumed_calories']} kcal\n"

            f"Remaining Calories : {summary['remaining_calories']} kcal\n\n"

            f"Protein : {summary['protein']} g\n"

            f"Carbohydrates : {summary['carbs']} g\n"

            f"Fat : {summary['fat']} g\n\n"

            f"Water Intake : {summary['water']} ml\n"

            f"Calories Burned : {summary['calories_burned']} kcal"

        )

        self.daily_summary_text.insert(

            tk.END,

            text

        )

        self.daily_summary_text.config(

            state="disabled"

        )

    # -------------------------------------------------

    def generate_weekly_summary(self):

     summary = self.controller.weekly_summary_report(

        self.get_selected_user_id(),

        self.date.get()

     )

     self.weekly_summary_text.config(

        state="normal"

     )

     self.weekly_summary_text.delete(

        "1.0",

        tk.END

     )

     if not summary["has_data"]:

        text = (

            "No meal records found\n"

            "for the selected week."

        )

     else:

        text = (

            f"Average Calories : {summary['average']} kcal\n"

            f"Maximum Calories : {summary['maximum']} kcal\n"

            f"Minimum Calories : {summary['minimum']} kcal\n"

            f"Median Calories : {summary['median']} kcal\n"

            f"Standard Deviation : {summary['standard_deviation']}"

        )

     self.weekly_summary_text.insert(

        tk.END,

        text

    )

     self.weekly_summary_text.config(

        state="disabled"

    )

    # -------------------------------------------------
   

    def select_meal(self, event):

        selected = self.tree.focus()

        if not selected:

            return

        values = self.tree.item(

            selected,

            "values"

        )

        self.meal.set(values[0])

        self.food_name.set(values[1])

        self.servings.set(values[2])

    # -------------------------------------------------

    def clear_fields(self):

        self.meal.set("Breakfast")

        self.food_combobox.current(0)

        self.servings.set(1)

        self.water.set(0)

        self.calories_burned.set(0)

        self.refresh_table()

        self.refresh_dashboard()