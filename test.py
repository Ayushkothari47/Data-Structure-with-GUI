import tkinter as tk
root = tk.Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
print(f"Screen width: {screen_width}px")
print(f"Screen height: {screen_height}px")
root.destroy()
