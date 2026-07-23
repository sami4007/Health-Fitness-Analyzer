from tkinter import ttk


def apply_theme(root):

    style = ttk.Style(root)

    # Use Windows theme
    style.theme_use("vista")

    # Fonts
    style.configure(
        ".",
        font=("Segoe UI", 10)
    )

    # LabelFrame
    style.configure(
        "TLabelframe",
        padding=12
    )

    style.configure(
        "TLabelframe.Label",
        font=("Segoe UI", 11, "bold")
    )

    # Buttons
    style.configure(
        "TButton",
        font=("Segoe UI", 10, "bold"),
        padding=(10, 6)
    )

    # Treeview
    style.configure(
        "Treeview",
        rowheight=28,
        font=("Segoe UI", 10)
    )

    style.configure(
        "Treeview.Heading",
        font=("Segoe UI", 10, "bold")
    )