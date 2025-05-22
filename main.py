import tkinter as tk
from tkinter import filedialog
import ttkbootstrap as ttk
from ttkbootstrap import Style
from PIL import Image, ImageDraw, ImageFont


def validate_spinbox(string, new_string):
    if len(new_string) > 3:
        return False
    return string.isdecimal()

def check_if_not_empty(string):
    if len(string) == 0:
        return False
    else:
        return True


class WatermarkGUI(tk.Tk):
    def __init__(self, title, size):
        super().__init__()
        self.config(padx=20, pady=20)
        self.geometry(f"{size[0]}x{size[1]}")
        self.minsize(size[0], size[1])
        self.style = Style(theme='darkly')
        self.title(title)

        # Widgets
        self.main = Main(self)


        self.mainloop()

class Main(ttk.Frame):
    def __init__(self, parent):
        super().__init__()
        self.create_widgets()
        self.layout_widgets()


        self.pack(fill='both', expand=True)


    # ---------------------------------------------------- WIDGETS ----------------------------------------------------#
    def create_widgets(self):
        # Top frame
        self.top_frame = ttk.Frame(self)

        ## Title label
        self.title_label = ttk.Label(self.top_frame, text='Watermark your image', font=('Helvetica', 24))

        # Middle frame
        self.middle_frame = ttk.Frame(self)
        ## File input widgets
        self.input_label = ttk.Label(
            self.middle_frame, 
            text='Select image to overlay:', 
            font=('Helvetica', 18), 
            justify='left')
        self.m1_frame = ttk.Frame(self.middle_frame)
        self.input_file_entry = ttk.Entry(self.m1_frame, font=20)
        self.input_file_button = ttk.Button(self.m1_frame, text="Browse", command=self.input_browse_func)

        ## File output widgets
        self.output_label = ttk.Label(self.middle_frame,
                                      text='Select path to save the image:',
                                      font=('Helvetica', 18),
                                      justify='left')
        self.m2_frame = ttk.Frame(self.middle_frame)
        self.output_file_entry = ttk.Entry(self.m2_frame, font=20)
        self.output_file_button = ttk.Button(self.m2_frame, text="Browse", command=self.output_browse_func)

        ## Widgets for watermark text
        self.watermark_text_label = ttk.Label(self.middle_frame,
                                              text='Text to overlay:',
                                              font=('Helvetica', 18),
                                              justify='left')
        self.m3_frame = ttk.Frame(self.middle_frame)
        self.watermark_text_entry = ttk.Entry(self.m3_frame, font=('Helvetica', 18))
        self.watermark_text_entry.insert(tk.END, 'Watermark')

        ## Font formatting widgets
        ### Font style combobox
        self.m4_frame = ttk.Frame(self.middle_frame)
        self.font_style_label = ttk.Label(self.m4_frame, text='Font: ', font=('Helvetica', 18), justify='left')
        self.combo_value = tk.StringVar()
        self.font_combo = ttk.Combobox(self.m4_frame, textvariable=self.combo_value, state='readonly', width=15)
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

        ### Font size spinbox
        self.m5_frame = ttk.Frame(self.middle_frame)
        self.font_size_label = ttk.Label(self.m5_frame, text='Size: ', font=('Helvetica', 18), justify='left')
        self.spinbox_val = tk.IntVar()
        self.spinbox_val.set("100")
        self.font_size_spinbox = ttk.Spinbox(self.m5_frame,
                                             textvariable=self.spinbox_val,
                                             from_=0,
                                             to=999,
                                             increment=10,
                                             validate="key",
                                             validatecommand=(self.register(validate_spinbox), "%S", "%P"),
                                             width=15)

        # Bottom frame
        self.bottom_frame = ttk.Frame(self)

        ## Status info
        self.status_label = ttk.Label(self.bottom_frame, text="", justify='center')

        ## Submit button
        self.submit_button = ttk.Button(self.bottom_frame, text='Submit', width=20, command=self.add_watermark)

    def layout_widgets(self):

        # Top frame
        ## Title label
        self.title_label.pack(padx=30, pady=(0, 30))
        self.top_frame.pack()

        # Middle frame
        ## File input widgets
        self.input_label.pack(pady=10)
        self.input_file_entry.pack(side='left', expand=True, fill='x')
        self.input_file_button.pack(side='left')
        self.m1_frame.pack(expand=True, fill='x')

        ## File output widgets
        self.output_label.pack(pady=10)
        self.output_file_entry.pack(side='left', expand=True, fill='x')
        self.output_file_button.pack(side='left')
        self.m2_frame.pack(expand=True, fill='x')

        ## Widgets for watermark text
        self.watermark_text_label.pack(pady=10)
        self.watermark_text_entry.pack(side='left', expand=True, fill='x')
        self.m3_frame.pack(expand=True, fill='x')

        ## Font formatting widgets
        ### Font style combobox
        self.font_style_label.pack(pady=10)
        self.font_combo.pack(side='left', expand=True, fill='x')
        self.m4_frame.pack(side='left', expand=True, fill='x', padx=10, pady=10)

        ### Font size spinbox
        self.font_size_label.pack(pady=10)
        self.font_size_spinbox.pack(side='left', expand=True, fill='x')
        self.m5_frame.pack(side='left', expand=True, fill='x')
        self.middle_frame.pack(expand=True, fill='x', padx=10)

        # Bottom frame
        ## Status info
        self.status_label.pack(expand=True, fill='x', padx=10, pady=10)

        ## Submit button
        self.submit_button.pack()
        self.bottom_frame.pack()

    #--------------------------------------------------- FUNCTIONS ---------------------------------------------------#
    def input_browse_func(self):
        self.file_path = tk.filedialog.askopenfilename(filetypes=(
            ("JPEG files",".jpeg .jpg"),
            ("PNG files", ".png"),
            ("BMP files", ".bmp"),
            ("All files","*.*")
            )
        )
        self.input_file_entry.insert(tk.END, self.file_path)
        self.output_file_entry.insert(tk.END, self.get_file_dir())

    def get_file_dir(self):
        dir_str_list = self.input_file_entry.get().split('/')
        return f'{"/".join(dir_str_list[:-1])}/'

    def output_browse_func(self):
            dirname = tk.filedialog.askdirectory(initialdir=self.get_file_dir())
            self.output_file_entry.insert(tk.END, dirname)

    def get_full_output_path(self):
        input_path = self.input_file_entry.get()
        output_path = self.output_file_entry.get()
        file_name = input_path.split('/')[-1]
        file_name_elements = file_name.split(".")
        file_name_new = f'{".".join(file_name_elements[:-1])}_watermarked.png'
        full_output_path = f'{output_path}{file_name_new}'
        return full_output_path

    def add_watermark(self):
        image = Image.open(self.input_file_entry.get(), mode='r')
        image = image.convert('RGBA')
        width, height = image.size

        # file_name = image_path.split('/')[-1].split('.')
        # output_file_name = f"{".".join(file_name[:-1])}_watermark.{file_name[-1]}"

        overlay = Image.new('RGBA', image.size, (255, 255, 255, 0))
        draw = ImageDraw.Draw(overlay)

        watermark_lines_color = (255, 255, 255, 30)

        for i in range(0, width + height, 50):
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
        watermark_font = font_dict[self.combo_value.get()]  # placeholder to input
        # font_size = 100 # placeholder to input
        font_size = self.spinbox_val.get()
        watermark_text = self.watermark_text_entry.get()
        font = ImageFont.truetype(watermark_font, font_size)
        text_width = font.getmask(watermark_text).getbbox()[2]
        text_height = font.getmask(watermark_text).getbbox()[3]

        x = (width - text_width) // 2
        y = (height - text_height) // 2

        watermark_text_color = (255, 255, 255, 80)

        draw.text((x, y),
                  watermark_text,
                  fill=watermark_text_color,
                  font=font)
        output_image = Image.alpha_composite(image, overlay)

        output_image.save(self.get_full_output_path())
        output_image.show()

class Input(ttk.Frame)

if __name__ == '__main__':
    gui = WatermarkGUI('Watermark Tool', (600,800))

