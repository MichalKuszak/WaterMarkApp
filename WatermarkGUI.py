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


class WatermarkGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.config(padx=20, pady=20)
        self.style = Style(theme='darkly')
        self.root.title('Watermark')
        # title
        self.window_title()
        # select input directory
        self.file_input_widgets()
        # select output directory
        self.file_saving_widgets()
        # entry for watermark text
        self.watermark_text_widgets()
        # font and font_size selection
        self.font_size_widgets()
        ## Combobox
        self.font_selection_combo()
        # status label
        self.warning_label()
        # submit button
        self.print_button()

        self.root.mainloop()

    # ----- WIDGETS -----#
    def window_title(self):
        self.title_label = ttk.Label(self.root, text='Watermark your image', font=('Helvetica', 24))
        self.title_label.grid(row=0, column=0, columnspan=4, padx=30, pady=(0, 30))

    def file_input_widgets(self):
        # Label
        self.input_label = ttk.Label(self.root, text='Select image to overlay:', font=('Helvetica', 18), justify='left')
        self.input_label.grid(row=1, column=0, columnspan=4, sticky='W')

        # Entry
        self.input_file_entry = ttk.Entry(self.root, font=20)
        self.input_file_entry.grid(row=2, column=0, columnspan=3, sticky='WE')

        # Button
        self.input_file_button = ttk.Button(self.root, text="Browse", command=self.input_browse_func)
        self.input_file_button.grid(row=2, column=3, sticky='WE', pady=10)

    def file_saving_widgets(self):
        ## Label
        self.output_label = ttk.Label(self.root, text='Select path to save the image:', font=('Helvetica', 18),
                                      justify='left')
        self.output_label.grid(row=3, column=0, columnspan=4, sticky='W')

        ## Entry
        self.output_file_entry = ttk.Entry(self.root, font=20)
        self.output_file_entry.grid(row=4, column=0, columnspan=3, sticky='WE')

        ## Button
        self.output_file_button = ttk.Button(self.root, text="Browse", command=self.output_browse_func)
        self.output_file_button.grid(row=4, column=3, sticky='WE', pady=10)

        # entry for watermark text

    def watermark_text_widgets(self):
        ## Label
        self.watermark_text_label = ttk.Label(self.root, text='Text to overlay: ', font=('Helvetica', 18),
                                              justify='left')
        self.watermark_text_label.grid(row=5, column=0, columnspan=4, sticky='W')

        ## Entry
        self.watermark_text_entry = ttk.Entry(self.root, font=18)
        self.watermark_text_entry.insert(tk.END, 'Watermark')
        self.watermark_text_entry.grid(row=6, column=0, columnspan=4, sticky='WE', pady=10)

    def font_size_widgets(self):
        ## Label
        self.font_size_label = ttk.Label(self.root, text='Size: ', font=('Helvetica', 18), justify='left')
        self.font_size_label.grid(row=7, column=2, sticky='W')

        ## Spinbox
        self.spinbox_val = tk.IntVar()
        self.spinbox_val.set("100")
        self.font_size_spinbox = ttk.Spinbox(self.root,
                                             textvariable=self.spinbox_val,
                                             from_=0,
                                             to=999,
                                             increment=10,
                                             validate="key",
                                             validatecommand=(self.root.register(validate_spinbox), "%S", "%P"))
        self.font_size_spinbox.grid(row=7, column=3, sticky='WE', pady=10)

    def font_selection_combo(self):
        ## Label
        self.fonttype_label = ttk.Label(self.root, text='Font: ', font=('Helvetica', 18), justify='left')
        self.fonttype_label.grid(row=7, column=0, sticky='W')
        ## Combobox
        self.combo_value = tk.StringVar()
        self.font_combo = ttk.Combobox(self.root, textvariable=self.combo_value, state='readonly', width=15)
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
        self.font_combo.grid(row=7, column=1, sticky='W', padx=(0,10))
    def warning_label(self):
        self.status_label = ttk.Label(self.root, text="", justify='center')
        self.status_label.grid(row=8, column=1, columnspan=2, pady=15, sticky="WE")
    def print_button(self):
        # submit button
        self.submit_button = ttk.Button(self.root, text='Submit', width=20, command=self.add_watermark)
        self.submit_button.grid(row=9, column=1, columnspan=3, pady=15)

    #----- FUNCTIONS -----#
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


if __name__ == '__main__':
    gui = WatermarkGUI()

