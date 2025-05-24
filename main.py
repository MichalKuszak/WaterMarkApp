import tkinter as tk
from email.policy import default
from tkinter import filedialog
import ttkbootstrap as ttk
from ttkbootstrap import Style
from PIL import Image, ImageDraw, ImageFont, ImageTk, UnidentifiedImageError
from pathlib import Path
# TODO: Add Drag & Drop Support


def validate_spinbox(string, new_string):
    if len(new_string) > 3:
        return False
    return string.isdecimal()


class GUI(tk.Tk):
    def __init__(self, title, size):
        super().__init__()
        self.config(padx=20, pady=20)
        self.geometry(f"{size[0]}x{size[1]}")
        self.minsize(size[0], size[1])
        self.style = Style()
        self.style.theme_use('darkly')
        self.title(title)

        # Widgets
        self.main = Main(self)
        self.main.darkmode_toggle.darkmode_spinbox.config(command=self.toggle_dark_mode)

    def toggle_dark_mode(self):
        if self.main.darkmode_toggle.darkmode_spinbox_val.get() == "ON":
            self.style.theme_use('darkly')
        else:
            self.style.theme_use('morph')


class Main(ttk.Frame):
    def __init__(self, parent):
        super().__init__()
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)

        self.create_widgets()
        self.layout_widgets()

        self.pack(fill='both', expand=True)

    # ---------------------------------------------------- WIDGETS ----------------------------------------------------#
    def create_widgets(self):

        # Frame #1
        self.frame_1 = ttk.Frame(self)
        self.darkmode_toggle = DarkModeToggle(self.frame_1)
        self.title_label = ttk.Label(self.frame_1, text='Watermark your image', font=('Helvetica', 20))
        self.canvas = ImageCanvas(self.frame_1)

        # Frame #2
        self.frame_2 = ttk.Frame(self)
        self.input_label = ttk.Label(
            self.frame_2,
            text='Select image to overlay:', 
            font=('Helvetica', 16), 
            justify='left')
        self.input = PathEntry(self.frame_2)
        self.output_label = ttk.Label(self.frame_2,
                                      text='Select path to save the image:',
                                      font=('Helvetica', 16),
                                      justify='left')
        self.output = PathEntry(self.frame_2)
        self.watermark_text = TextEntry(self.frame_2)
        self.font_style = FontCombo(self.frame_2)

        self.font_size = FontSpin(self.frame_2)

        # Frame #3
        self.frame_3 = ttk.Frame(self)
        self.status_label = ttk.Label(self.frame_3, justify='center', font=("Helvetica", 16, "bold"),
                                      foreground="red")
        self.submit_button = ttk.Button(self.frame_3, text='Submit', width=20, style='success')
        self.preview_button = ttk.Button(self.frame_3, text='Preview', width=20, bootstyle='info-outline')

    def layout_widgets(self):
        # Frame #1
        self.darkmode_toggle.pack(side="top", anchor="ne")
        self.title_label.pack(pady=10)
        self.canvas.pack()
        self.frame_1.grid(row=1, column=0, sticky="NEWS")

        # Frame #2
        self.input_label.pack(pady=10)
        self.input.pack(fill='x', expand=True)
        self.output_label.pack(pady=10)
        self.output.pack(expand=True, fill='x')
        self.watermark_text.pack(expand=True, fill='x')
        self.font_style.pack(side='left', expand=True, fill='x', padx=10, pady=10)
        self.font_size.pack(side='left', expand=True, fill='x')
        self.frame_2.grid(row=2, column=0, sticky="NEWS")

        # Frame #3
        self.status_label.pack(pady=10)
        self.submit_button.pack(pady=10)
        self.preview_button.pack()
        self.frame_3.grid(row=3, column=0, sticky="NEW")

class ImageCanvas(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.canvas_create_widgets()
        self.canvas_layout_widgets()

    def canvas_create_widgets(self):
        self.canvas = ttk.Canvas(self, width= 400, height=225, background="red", bd=0, highlightthickness=0, relief="ridge")
        self.open_img = Image.open("./assets/mark.jpg").resize((400,225))
        self.img = ImageTk.PhotoImage(self.open_img)
        self.canvas.create_image(200,150, image=self.img)

    def canvas_layout_widgets(self):
        self.canvas.pack(expand=True, fill="both")

    def update_image(self, pil_image):
        self.img = ImageTk.PhotoImage(pil_image.resize((400, 225)))
        self.canvas.delete("all")
        self.canvas.create_image(200, 150, image=self.img)
        self.canvas.image = self.img

class DarkModeToggle(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.toggle_create_widgets()
        self.toggle_layout_widgets()

    def toggle_create_widgets(self):
        self.darkmode_label = ttk.Label(self, text='Dark Mode:', font=('Helvetica', 12), justify='left')
        self.darkmode_spinbox_val = tk.StringVar()
        self.darkmode_spinbox_val.set("ON")
        self.darkmode_spinbox = ttk.Spinbox(self,
                                             values=["ON", "OFF"],
                                             textvariable=self.darkmode_spinbox_val,
                                             state='readonly',
                                            width=5,
                                            wrap=True)

    def toggle_layout_widgets(self):
        self.darkmode_label.pack(side='left', expand=True, fill='x')
        self.darkmode_spinbox.pack(side='left')


class PathEntry(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.entry_create_widgets()
        self.entry_layout_widgets()

    def entry_create_widgets(self):
        self.path_entry = ttk.Entry(self, font=16)
        self.browse_button = ttk.Button(self, text="Browse")

    def entry_layout_widgets(self):
        self.path_entry.pack(side='left', expand=True, fill='x')
        self.browse_button.pack(side='left')


class TextEntry(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.entry_create_widgets()
        self.entry_layout_widgets()

    def entry_create_widgets(self):
        self.watermark_text_label = ttk.Label(self,
                                              text='Text to overlay:',
                                              font=('Helvetica', 16),
                                              justify='left')
        self.watermark_text_entry = ttk.Entry(self, font=('Helvetica', 16))
        self.watermark_text_entry.insert(tk.END, 'Watermark')

    def entry_layout_widgets(self):
        self.watermark_text_label.pack(pady=10)
        self.watermark_text_entry.pack(side='left', expand=True, fill='x')


class FontCombo(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.font_style_create_widgets()
        self.font_style_layout_widgets()

    def font_style_create_widgets(self):
        self.font_style_label = ttk.Label(self, text='Font: ', font=('Helvetica', 16), justify='left')
        self.combo_value = tk.StringVar()
        self.font_combo = ttk.Combobox(self, textvariable=self.combo_value, state='readonly', width=15)
        self.font_combo['values'] = ('Helvetica',
                                          'Times New Roman',
                                          'Georgia',
                                          'Comic Sans',
                                          'Verdana',
                                          'Arial',
                                          'Baskerville',
                                          'Futura',
                                          'Bodoni',
                                          'Rockwell')
        self.font_combo.current(0)

    def font_style_layout_widgets(self):
        self.font_style_label.pack(pady=10)
        self.font_combo.pack(side='left', expand=True, fill='x')

class FontSpin(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.font_size_create_widgets()
        self.font_size_layout_widgets()

    def font_size_create_widgets(self):
        self.font_size_label = ttk.Label(self, text='Size: ', font=('Helvetica', 16), justify='left')
        self.spinbox_val = tk.IntVar()
        self.spinbox_val.set(100)
        self.font_size_spinbox = ttk.Spinbox(self,
                                             textvariable=self.spinbox_val,
                                             from_=0,
                                             to=999,
                                             increment=10,
                                             validate="key",
                                             validatecommand=(self.register(validate_spinbox), "%S", "%P"),
                                             width=15)

    def font_size_layout_widgets(self):
        self.font_size_label.pack(pady=10)
        self.font_size_spinbox.pack(side='left', expand=True, fill='x')

class Watermarker(GUI):
    def __init__(self, title, size):
        super().__init__(title=title, size=size)

    def add_watermark(self):
        LINE_ALPHA = 80
        LINE_SPACING = 50

        try:
            with Image.open(self.main.input.path_entry.get(), mode='r') as img:
                img.verify()
        except (UnidentifiedImageError, FileNotFoundError):
            self.main.status_label.configure(text="The image file you selected is unsupported!")
            return
        except IsADirectoryError:
            self.main.status_label.configure(text="You selected a directory, not an image file!")
            return

        image = Image.open(self.main.input.path_entry.get(), mode='r')
        image = image.convert('RGBA')
        width, height = image.size

        overlay = Image.new('RGBA', image.size, (255, 255, 255, 0))
        draw = ImageDraw.Draw(overlay)

        watermark_lines_color = (255, 255, 255, 30)

        for i in range(0, width + height, LINE_SPACING):
            draw.line(((0, height - i), (i, height)),
                      fill=watermark_lines_color,
                      width=5)

        font_dict = {'Helvetica': 'Helvetica.ttc',
                     'Times New Roman': 'Times New Roman.ttf',
                     'Georgia': 'Georgia.ttf',
                     'Comic Sans': 'Comic Sans MS.ttf',
                     'Verdana': 'Verdana.ttf',
                     'Arial': 'Arial.ttf',
                     'Baskerville': 'Baskerville.ttc',
                     'Futura': 'Futura.ttc',
                     'Bodoni': 'Bodoni 72.ttc',
                     'Rockwell': 'Rockwell.ttc'
                     }
        watermark_font = font_dict[self.main.font_style.combo_value.get()]

        font_size = self.main.font_size.spinbox_val.get()
        watermark_text = self.main.watermark_text.watermark_text_entry.get()
        try:
            font = ImageFont.truetype(watermark_font, font_size)
        except IOError:
            self.main.status_label.configure(text="Font not found, using default font")
            font = ImageFont.load_default(font_size)
        text_width = font.getmask(watermark_text).getbbox()[2]
        text_height = font.getmask(watermark_text).getbbox()[3]

        x = (width - text_width) // 2
        y = (height - text_height) // 2

        watermark_text_color = (255, 255, 255, LINE_ALPHA)

        draw.text((x, y),
                  watermark_text,
                  fill=watermark_text_color,
                  font=font)
        self.output_image = Image.alpha_composite(image, overlay)
        self.main.canvas.update_image(self.output_image)

    def validate_and_preview(self):
        input_path = self.main.input.path_entry.get().strip()
        output_path = self.main.output.path_entry.get().strip()

        if len(input_path) == 0 and len(output_path) == 0:
            self.main.status_label.configure(text="Please select the image file and saving directory!")
        elif len(input_path) == 0:
            self.main.status_label.configure(text="Please select the image file!")
        elif len(output_path) == 0:
            self.main.status_label.configure(text="Please select the saving directory!")
        else:
            self.main.status_label.configure(text="")
            self.add_watermark()




class App(Watermarker):
    def __init__(self, title, size):
        super().__init__(title=title, size=size)
        self.main.input.browse_button.config(command=self.browse_input_file)
        self.main.output.browse_button.config(command=self.browse_saving_dir)
        self.main.submit_button.config(command=self.save_file)
        self.main.preview_button.config(command=self.validate_and_preview)


    def browse_input_file(self):
        self.file_path = Path(tk.filedialog.askopenfilename(filetypes=(
            ("JPEG files",".jpeg .jpg"),
            ("PNG files", ".png"),
            ("BMP files", ".bmp"),
            ("All files","*.*")
            )))
        self.input_path = self.file_path.absolute()
        self.output_dir = self.file_path.parent
        self.main.input.path_entry.delete(0, tk.END)
        self.main.input.path_entry.insert(tk.END, f"{self.input_path}")
        self.main.output.path_entry.delete(0, tk.END)
        self.main.output.path_entry.insert(tk.END, f"{self.output_dir}")


    def browse_saving_dir(self):
        dirname = tk.filedialog.askdirectory(initialdir=self.output_dir)
        self.output_dir = Path(dirname)
        self.main.output.path_entry.delete(0, tk.END)
        self.main.output.path_entry.insert(tk.END, dirname)

    def unique_path(self, directory, name_pattern):
        counter = 0
        while True:
            counter += 1
            path = directory / name_pattern.format(counter)
            if not path.exists():
                return path


    def save_file(self):
        self.validate_and_preview()
        template = f"{self.input_path.stem}"+"{:03d}_watermarked.png"
        self.output_image.save(self.unique_path(self.output_dir, template))

if __name__ == '__main__':
    gui = App('Watermark Tool', (600,800))
    gui.mainloop()
