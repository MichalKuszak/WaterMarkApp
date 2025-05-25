import tkinter as tk
from tkinter import filedialog
import ttkbootstrap as ttk
from ttkbootstrap import Style
from PIL import Image, ImageDraw, ImageFont, ImageTk, UnidentifiedImageError
from pathlib import Path
from tkinterdnd2 import DND_FILES, TkinterDnD


root = TkinterDnD.Tk()  # notice - use this instead of tk.Tk()

lb = tk.Listbox(root)
lb.insert(1, "drag files to here")

# register the listbox as a drop target
lb.drop_target_register(DND_FILES)
lb.dnd_bind('<<Drop>>', lambda e: lb.insert(tk.END, e.data))

lb.pack()
root.mainloop()
