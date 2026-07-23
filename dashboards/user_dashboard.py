import tkinter as tk
from tkinter import ttk, messagebox

from config import (
    WINDOW_TITLE,
    WINDOW_WIDTH,
    WINDOW_HEIGHT,
    ACTIVITY_LEVELS,
    GOALS
)

from controllers.user_controller import UserController


class UserDashboard:

    def __init__(self, root):

        self.root = root
        self.controller = UserController()

        self.root.title(WINDOW_TITLE)
        self.root.geometry("1200x800")
        self.root.resizable(False, False)
        self.root.configure(
        bg="#F5FAFD"
        )

        self.create_variables()
        self.create_widgets()
        self.refresh_table()

    # -------------------------------------------------

    def create_variables(self):

        self.user_id = tk.StringVar()

        self.name = tk.StringVar()

        self.age = tk.StringVar()

        self.gender = tk.StringVar(value="Male")

        self.height = tk.StringVar()

        self.weight = tk.StringVar()

        self.activity = tk.StringVar(value=ACTIVITY_LEVELS[0])

        self.goal = tk.StringVar(value=GOALS[0])

        self.search_id = tk.StringVar()

    # -------------------------------------------------

    def create_widgets(self):

        # ==========================
        # Header
        # ==========================
        self.create_title()

        # ==========================
        # Main Container
        # ==========================
        self.content_frame = tk.Frame(
            self.root,
            bg="#F5FAFD"
        )

        self.content_frame.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=(10, 15)
        )

        # Grid Layout
        self.content_frame.columnconfigure(
            0,
            weight=5
        )

        self.content_frame.columnconfigure(
            1,
            weight=2
        )

        self.content_frame.rowconfigure(0, weight=0)
        self.content_frame.rowconfigure(1, weight=0)
        self.content_frame.rowconfigure(2, weight=0)
        self.content_frame.rowconfigure(3, weight=1)

        # ==========================
        # Build UI
        # ==========================
        self.create_user_frame()
        self.create_button_frame()
        self.create_search_frame()
        self.create_dashboard_cards()
        self.create_table()
        self.create_status_bar()

    # -------------------------------------------------

    def create_title(self):

        title_frame = tk.Frame(
            self.root
        )

        title_frame.pack(
            pady=(15, 5)
        )

        title = tk.Label(
            title_frame,
            text="🏃 Health Fitness & Calorie Tracker",
            font=("Segoe UI", 20, "bold"),
            fg="#114B5F"
        )

        title.pack()

        subtitle = tk.Label(
            title_frame,
            text="User Management Dashboard",
            font=("Segoe UI", 11)
        )

        subtitle.pack(pady=(5, 0))


    # -------------------------------------------------

    def create_user_frame(self):

        frame = ttk.LabelFrame(
            self.content_frame,
            text="👤 User Information",
            padding=15
        )

        frame.grid(
            row=0,
            column=0,
            sticky="nsew",
            padx=(0, 10),
            pady=(0, 10)
        )

        self.content_frame.columnconfigure(0, weight=3)

        frame.columnconfigure(1, weight=1)
        frame.columnconfigure(3, weight=1)

        fields = [

            ("User ID", self.user_id, "entry_readonly"),
            ("Name", self.name, "entry"),

            ("Age", self.age, "entry"),
            ("Gender", None, "gender"),

            ("Height (cm)", self.height, "entry"),
            ("Weight (kg)", self.weight, "entry"),

            ("Activity", self.activity, "activity"),
            ("Goal", self.goal, "goal")

        ]

        row = 0

        for i in range(0, len(fields), 2):

            left = fields[i]
            right = fields[i + 1]

            ttk.Label(frame, text=left[0]).grid(
                row=row,
                column=0,
                padx=5,
                pady=8,
                sticky="w"
            )

            self.create_field(frame, left, row, 1)

            ttk.Label(frame, text=right[0]).grid(
                row=row,
                column=2,
                padx=5,
                pady=8,
                sticky="w"
            )

            self.create_field(frame, right, row, 3)

            row += 1

    # -------------------------------------------------

    def create_field(self, parent, field, row, column):

        label, variable, field_type = field

        # -----------------------------
        # Readonly Entry
        # -----------------------------
        if field_type == "entry_readonly":

            ttk.Entry(
                parent,
                textvariable=variable,
                state="readonly",
                width=28
            ).grid(
                row=row,
                column=column,
                sticky="ew",
                padx=3,
                pady=3
            )

        # -----------------------------
        # Normal Entry
        # -----------------------------
        elif field_type == "entry":

            ttk.Entry(
                parent,
                textvariable=variable,
                width=28
            ).grid(
                row=row,
                column=column,
                sticky="ew",
                padx=3,
                pady=3
            )

        # -----------------------------
        # Gender
        # -----------------------------
        elif field_type == "gender":

            gender_frame = ttk.Frame(parent)

            gender_frame.grid(
                row=row,
                column=column,
                sticky="w",
                padx=3,
                pady=3
            )

            ttk.Radiobutton(
                gender_frame,
                text="Male",
                variable=self.gender,
                value="Male"
            ).pack(side="left")

            ttk.Radiobutton(
                gender_frame,
                text="Female",
                variable=self.gender,
                value="Female"
            ).pack(side="left", padx=(10, 0))

        # -----------------------------
        # Activity
        # -----------------------------
        elif field_type == "activity":

            ttk.Combobox(
                parent,
                textvariable=self.activity,
                values=ACTIVITY_LEVELS,
                state="readonly"
            ).grid(
                row=row,
                column=column,
                sticky="ew",
                padx=3,
                pady=3
            )

        # -----------------------------
        # Goal
        # -----------------------------
        elif field_type == "goal":

            ttk.Combobox(
                parent,
                textvariable=self.goal,
                values=GOALS,
                state="readonly"
            ).grid(
                row=row,
                column=column,
                sticky="ew",
                padx=3,
                pady=3
            )

    # -------------------------------------------------

    def create_button_frame(self):

        frame = ttk.LabelFrame(
            self.content_frame,
            text="⚡ Quick Actions",
            padding=12
        )

        frame.grid(
            row=0,
            column=1,
            sticky="nsew",
            pady=(0, 10),
            padx=(5, 0)
        )

        frame.columnconfigure(0, weight=1)

        # Inner frame
        button_frame = ttk.Frame(frame)
        button_frame.pack(expand=True, fill="x")

        buttons = [

            ("➕ Add User", self.add_user),
            ("✏ Update User", self.update_user),
            ("🗑 Delete User", self.delete_user),
            ("🧹 Clear Fields", self.clear_fields)

        ]

        for text, command in buttons:

            ttk.Button(
                button_frame,
                text=text,
                command=command,
                width=18
            ).pack(
                fill="x",
                pady=3,
                ipady=1
            )

    # -------------------------------------------------

    def create_search_frame(self):

        frame = ttk.LabelFrame(
            self.content_frame,
            text="🔍 Search User",
            padding=15
        )

        frame.grid(
            row=1,
            column=0,
            columnspan=2,
            sticky="ew",
            pady=(0, 10)
        )

        frame.columnconfigure(1, weight=1)

        ttk.Label(
            frame,
            text="User ID"
        ).grid(
            row=0,
            column=0,
            padx=(5, 10),
            pady=5,
            sticky="w"
        )

        ttk.Entry(
            frame,
            textvariable=self.search_id
        ).grid(
            row=0,
            column=1,
            sticky="ew",
            padx=5
        )

        ttk.Button(
            frame,
            text="🔍 Search",
            command=self.search_user
        ).grid(
            row=0,
            column=2,
            padx=(10, 5)
        )

    # -------------------------------------------------

    def create_dashboard_cards(self):

        frame = tk.Frame(
            self.content_frame,
            bg="#F5FAFD"
        )

        frame.grid(
            row=2,
            column=0,
            columnspan=2,
            sticky="ew",
            pady=(0, 10)
        )

        for i in range(3):
            frame.columnconfigure(i, weight=1)

        self.total_users_value, self.total_users_sub = self.create_stat_card(
            frame,
            0,
            "👥",
            "Total Users",
            "0",
            "Registered"
        )

        self.avg_bmi_value, self.avg_bmi_sub = self.create_stat_card(
            frame,
            1,
            "📊",
            "Average BMI",
            "0.0",
            "Normal"
        )

        self.goal_value, self.goal_sub = self.create_stat_card(
            frame,
            2,
            "🎯",
            "Popular Goal",
            "-",
            "No Data"
        )
    # -------------------------------------------------

    def create_stat_card(self, parent, column, icon, title, value, subtitle):

        card = tk.Frame(
            parent,
            bg="white",
            bd=1,
            relief="solid"
        )

        card.grid(
            row=0,
            column=column,
            padx=8,
            sticky="nsew"
        )

        # Icon
        tk.Label(
            card,
            text=icon,
            font=("Segoe UI Emoji", 20),
            bg="white",
            fg="#1976D2"
        ).pack(pady=(4, 0))

        # Title
        tk.Label(
            card,
            text=title,
            font=("Segoe UI", 10),
            bg="white",
            fg="#666666"
        ).pack()

        # Main Value
        value_label = tk.Label(
            card,
            text=value,
            font=("Segoe UI", 18, "bold"),
            bg="white",
            fg="#114B5F"
        )

        value_label.pack(pady=(2, 0))

        # Subtitle
        subtitle_label = tk.Label(
            card,
            text=subtitle,
            font=("Segoe UI", 9),
            bg="white",
            fg="#888888"
        )

        subtitle_label.pack(pady=(0, 6))

        return value_label, subtitle_label

    # -------------------------------------------------

    def update_dashboard(self):

        users = self.controller.get_all_users()

        # -----------------------
        # Total Users
        # -----------------------
        total_users = len(users)

        self.total_users_value.config(
            text=str(total_users)
        )

        self.total_users_sub.config(
            text="Registered"
        )

        # -----------------------
        # Average BMI
        # -----------------------
        if total_users > 0:

            avg_bmi = sum(
                user["bmi"] for user in users
            ) / total_users

            self.avg_bmi_value.config(
                text=f"{avg_bmi:.1f}"
            )

            self.avg_bmi_sub.config(
                text="Average BMI"
            )

        else:

            self.avg_bmi_value.config(text="0.0")
            self.avg_bmi_sub.config(text="No Data")


    # -------------------------------------------------

    def create_table(self):

        table_frame = ttk.LabelFrame(
            self.content_frame,
            text="📋 User Records",
            padding=10
        )

        table_frame.grid(
            row=3,
            column=0,
            columnspan=2,
            sticky="nsew",
            pady=(0, 10)
        )

        table_frame.columnconfigure(0, weight=1)
        table_frame.rowconfigure(0, weight=1)

        columns = (
            "ID",
            "Name",
            "Age",
            "Gender",
            "BMI"
        )

        self.tree = ttk.Treeview(
            table_frame,
            columns=columns,
            show="headings",
            height=13
        )

        for col in columns:

            self.tree.heading(
                col,
                text=col
            )

            self.tree.column(
                col,
                anchor="center",
                width=130
            )

        scrollbar = ttk.Scrollbar(
            table_frame,
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

        self.tree.bind(
            "<Double-1>",
            self.select_user
        )

        self.tree.tag_configure(
            "even",
            background="#F8FBFD"
        )

        self.tree.tag_configure(
            "odd",
            background="white"
        )


    # -------------------------------------------------

    def refresh_table(self):

        # Clear existing rows
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Insert updated rows
        users = self.controller.get_all_users()

        for index, user in enumerate(users):

            tag = "even" if index % 2 == 0 else "odd"

            self.tree.insert(
                "",
                "end",
                values=(
                    user["user_id"],
                    user["name"],
                    user["age"],
                    user["gender"],
                    f'{user["bmi"]:.2f}'
                ),
                tags=(tag,)
            )

        self.update_dashboard()

    # -------------------------------------------------
    
    def select_user(self, event):

        selected = self.tree.focus()

        if not selected:
            return

        values = self.tree.item(selected, "values")

        user = self.controller.find_user(values[0])

        if user:

            self.user_id.set(user.user_id)
            self.name.set(user.name)
            self.age.set(user.age)
            self.gender.set(user.gender)
            self.height.set(user.height)
            self.weight.set(user.weight)
            self.activity.set(user.activity_level)
            self.goal.set(user.goal)
    
    # -------------------------------------------------
    

    
    def add_user(self):

        if (
            self.name.get() == "" or
            self.age.get() == "" or
            self.height.get() == "" or
            self.weight.get() == "" or
            self.activity.get() == "" or
            self.goal.get() == ""
        ):

            messagebox.showerror(
                "Error",
                "Please fill in all fields."
            )
            return

        try:

            user = self.controller.add_user(

                self.name.get(),

                int(self.age.get()),

                self.gender.get(),

                float(self.height.get()),

                float(self.weight.get()),

                self.activity.get(),

                self.goal.get()

            )

            messagebox.showinfo(
                "Success",
                f"{user.name} added successfully.\n\n"
                f"BMI : {user.bmi:.2f}\n"
                f"Category : {user.bmi_category}"
            )

            self.refresh_table()

            self.clear_fields()

        except ValueError:

            messagebox.showerror(
                "Error",
                "Age, Height and Weight must be numeric."
            )
            
    # -------------------------------------------------

    def update_user(self):

        if self.user_id.get() == "":

            messagebox.showwarning(
                "Warning",
                "Please select a user first."
            )

            return

        try:

            updated = self.controller.update_user(

                self.user_id.get(),

                self.name.get(),

                int(self.age.get()),

                self.gender.get(),

                float(self.height.get()),

                float(self.weight.get()),

                self.activity.get(),

                self.goal.get()

            )

            if updated:

                messagebox.showinfo(
                    "Success",
                    "User updated successfully."
                )

                self.refresh_table()

                self.clear_fields()

            else:

                messagebox.showerror(
                    "Error",
                    "User not found."
                )

        except ValueError:

            messagebox.showerror(
                "Error",
                "Age, Height and Weight must be numeric."
            )
    
    # -------------------------------------------------

    def delete_user(self):

        if self.user_id.get() == "":

            messagebox.showwarning(
                "Warning",
                "Please select a user first."
            )
            return

        confirm = messagebox.askyesno(
            "Confirm Delete",
            f"Delete user '{self.name.get()}'?"
        )

        if not confirm:
            return

        deleted = self.controller.delete_user(
            self.user_id.get()
        )

        if deleted:

            messagebox.showinfo(
                "Success",
                "User deleted successfully."
            )

            self.refresh_table()

            self.clear_fields()

        else:

            messagebox.showerror(
                "Error",
                "User not found."
            )
    
    # -------------------------------------------------

    def search_user(self):

        user_id = self.search_id.get().strip()

        if user_id == "":

            messagebox.showwarning(
                "Warning",
                "Enter a User ID."
            )
            return

        user = self.controller.find_user(user_id)

        if user:

            self.user_id.set(user.user_id)
            self.name.set(user.name)
            self.age.set(user.age)
            self.gender.set(user.gender)
            self.height.set(user.height)
            self.weight.set(user.weight)
            self.activity.set(user.activity_level)
            self.goal.set(user.goal)

            for item in self.tree.get_children():

                values = self.tree.item(item, "values")

                if values[0] == user.user_id:

                    self.tree.selection_set(item)
                    self.tree.focus(item)
                    self.tree.see(item)
                    break

        else:

            messagebox.showerror(
                "Not Found",
                "User not found."
            )
    
    # -------------------------------------------------

    def create_status_bar(self):

        self.status = tk.Label(

            self.root,

            text="Ready",

            anchor="w",

            relief="sunken",

            padx=10,

            font=("Segoe UI", 9)

        )

        self.status.pack(

            side="bottom",

            fill="x"

        )

    # -------------------------------------------------

    def clear_fields(self):

        self.user_id.set("")
        self.name.set("")
        self.age.set("")
        self.gender.set("Male")
        self.height.set("")
        self.weight.set("")
        self.activity.set("")
        self.goal.set("")
        self.search_id.set("")