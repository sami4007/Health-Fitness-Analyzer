import tkinter as tk

from assets.themes.style import apply_theme
from app import Application

root = tk.Tk()

apply_theme(root)

Application(root)

root.mainloop()