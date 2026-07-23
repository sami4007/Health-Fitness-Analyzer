import tkinter as tk
from assets.themes.style import apply_theme

from dashboards.user_dashboard import UserDashboard

root = tk.Tk()

apply_theme(root)

app = UserDashboard(root)

root.mainloop()