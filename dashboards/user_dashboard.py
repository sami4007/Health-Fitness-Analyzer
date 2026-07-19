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
        self.root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
        self.root.resizable(False, False)

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

        title = tk.Label(
            self.root,
            text="Health Fitness & Calorie Tracker",
            font=("Arial", 18, "bold")
        )

        title.pack(pady=10)

        subtitle = tk.Label(
            self.root,
            text="User Management Dashboard",
            font=("Arial", 12)
        )

        subtitle.pack()

        self.create_user_frame()

        self.create_button_frame()

        self.create_search_frame()

        self.create_table()

    # -------------------------------------------------

    def create_user_frame(self):

        frame = ttk.LabelFrame(
            self.root,
            text="User Information",
            padding=10
        )

        frame.pack(padx=20, pady=10)

        ttk.Label(frame, text="User ID").grid(row=0, column=0, padx=5, pady=5)

        ttk.Entry(
            frame,
            textvariable=self.user_id,
            state="readonly",
            width=30
        ).grid(row=0, column=1)

        ttk.Label(frame, text="Name").grid(row=0, column=2)

        ttk.Entry(
            frame,
            textvariable=self.name,
            width=30
        ).grid(row=0, column=3)

        ttk.Label(frame, text="Age").grid(row=1, column=0)

        ttk.Entry(
            frame,
            textvariable=self.age,
            width=30
        ).grid(row=1, column=1)

        ttk.Label(frame, text="Gender").grid(row=1, column=2)

        gender_frame = ttk.Frame(frame)

        gender_frame.grid(row=1, column=3)

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
        ).pack(side="left")

        ttk.Label(frame, text="Height (cm)").grid(row=2, column=0)

        ttk.Entry(
            frame,
            textvariable=self.height,
            width=30
        ).grid(row=2, column=1)

        ttk.Label(frame, text="Weight (kg)").grid(row=2, column=2)

        ttk.Entry(
            frame,
            textvariable=self.weight,
            width=30
        ).grid(row=2, column=3)

        ttk.Label(frame, text="Activity").grid(row=3, column=0)

        ttk.Combobox(
            frame,
            textvariable=self.activity,
            values=ACTIVITY_LEVELS,
            width=30,
            state="readonly"
        ).grid(row=3, column=1)

        ttk.Label(frame, text="Goal").grid(row=3, column=2)

        ttk.Combobox(
            frame,
            textvariable=self.goal,
            values=GOALS,
            width=30,
            state="readonly"
        ).grid(row=3, column=3)

    # -------------------------------------------------

    def create_button_frame(self):

        frame = ttk.Frame(self.root)

        frame.pack(pady=10)

        ttk.Button(
            frame,
            text="Add User",
            width=15,
            command=self.add_user
        ).grid(row=0, column=0, padx=5)

        ttk.Button(
            frame,
            text="Update",
            width=15,
            command=self.update_user
        ).grid(row=0, column=1, padx=5)

        ttk.Button(
            frame,
            text="Delete",
            width=15,
            command=self.delete_user
        ).grid(row=0, column=2, padx=5)

        ttk.Button(
            frame,
            text="Clear",
            width=15,
            command=self.clear_fields
        ).grid(row=0, column=3, padx=5)

    # -------------------------------------------------

    def create_search_frame(self):

        frame = ttk.LabelFrame(
            self.root,
            text="Search User",
            padding=10
        )

        frame.pack(fill="x", padx=20, pady=10)

        ttk.Label(
            frame,
            text="User ID"
        ).grid(row=0, column=0, padx=5)

        ttk.Entry(
            frame,
            textvariable=self.search_id,
            width=30
        ).grid(row=0, column=1)

        ttk.Button(
            frame,
            text="Search",
            command=self.search_user
        ).grid(row=0, column=2, padx=10)

    # -------------------------------------------------

    def create_table(self):

        frame = ttk.Frame(self.root)

        frame.pack(fill="both", expand=True, padx=20, pady=10)

        columns = (
            "ID",
            "Name",
            "Age",
            "Gender",
            "BMI"
        )

        self.tree = ttk.Treeview(
            frame,
            columns=columns,
            show="headings",
            height=12
        )

        for col in columns:

            self.tree.heading(col, text=col)

            self.tree.column(col, width=120, anchor="center")

        # Alternate row colors
        self.tree.tag_configure(
            "even",
            background="#F5F5F5"
        )

        self.tree.tag_configure(
            "odd",
            background="white"
        )

        scrollbar = ttk.Scrollbar(
            frame,
            orient="vertical",
            command=self.tree.yview
        )

        self.tree.configure(yscrollcommand=scrollbar.set)

        self.tree.pack(side="left", fill="both", expand=True)

        scrollbar.pack(side="right", fill="y")

        # Double-click to load user information
        self.tree.bind(
            "<Double-1>",
            self.select_user
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