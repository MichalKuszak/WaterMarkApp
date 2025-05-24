import tkinter as tk
from tkinter import filedialog
import ttkbootstrap as ttk
from ttkbootstrap import Style
from PIL import Image, ImageDraw, ImageFont, ImageTk

class Main(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("600x600")

        self.frame_1 = ttk.Frame(self)
        self.canvas = ImageCanvas(self.frame_1)

        self.canvas.pack()
        self.frame_1.pack()




if __name__ == '__main__':
    root = Main()
    root.mainloop()
