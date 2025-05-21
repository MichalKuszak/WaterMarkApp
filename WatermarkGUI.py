import tkinter as tk
from tkinter import filedialog
import ttkbootstrap as ttk
from ttkbootstrap import Style
from img_functions import add_watermark

class WatermarkGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.config(padx=20, pady=20)
        self.style = Style(theme='darkly')
        self.root.title('Watermark')

        self.input_file_val = tk.StringVar()
        self.output_dir_val = tk.StringVar()
        self.watermark_text_val = tk.StringVar()
        self.combo_val = tk.StringVar()
        self.fontsize_val = tk.StringVar()

        # title
        self.title_label = ttk.Label(self.root, text='Watermark your image', font=('Helvetica', 24))
        self.title_label.grid(row=0, column=0, columnspan=4, padx=30, pady=(0, 30))

        # select input directory
        ## Label
        self.input_label = ttk.Label(self.root, text='Select image to overlay:', font=('Helvetica', 18), justify='left')
        self.input_label.grid(row=1, column=0, columnspan=4, sticky='W')

        ## Entry
        self.input_file_entry = ttk.Entry(self.root, font=20, textvariable=self.input_file_val)
        self.input_file_entry.grid(row=2, column=0, columnspan=3, sticky='WE')

        ## Button
        self.input_file_button = ttk.Button(self.root, text="Browse", command=self.input_browse_func)
        self.input_file_button.grid(row=2, column=3, sticky='WE', pady=10)

        # select output directory
        ## Label
        self.output_label = ttk.Label(self.root, text='Select path to save the image:', font=('Helvetica', 18), justify='left')
        self.output_label.grid(row=3, column=0, columnspan=4, sticky='W')

        ## Entry
        self.output_file_entry = ttk.Entry(self.root, font=20, textvariable=self.output_dir_val)
        self.output_file_entry.grid(row=4, column=0, columnspan=3, sticky='WE')

        ## Button
        self.output_file_button = ttk.Button(self.root, text="Browse", command=self.output_browse_func)
        self.output_file_button.grid(row=4, column=3, sticky='WE', pady=10)

        # entry for watermark text
        ## Label
        self.watermark_text_label = ttk.Label(self.root, text='Text to overlay: ', font=('Helvetica', 18), justify='left')
        self.watermark_text_label.grid(row=5, column=0, columnspan=4, sticky='W')

        ## Entry
        self.watermark_text_entry = ttk.Entry(self.root, font=18, textvariable=self.watermark_text_val)
        self.watermark_text_entry.insert(tk.END, 'Watermark')
        self.watermark_text_entry.grid(row=6, column=0, columnspan=4, sticky='WE', pady=10)

        # font and fontsize selection
        ## Label
        self.fonttype_label = ttk.Label(self.root, text='Font: ', font=('Helvetica', 18), justify='left')
        self.fonttype_label.grid(row=7, column=0, sticky='W')

        ## Combobox
        self.font_combo = ttk.Combobox(self.root,
                                  state='readonly',
                                  values=['Helvetica',
                                          'Times New Roman',
                                          'Georgia',
                                          'Comic Sans',
                                          'Verdana',
                                          'Arial',
                                          'Baskerville',
                                          'Futura',
                                          'Bodoni',
                                          'Rockwell'],
                                  width=15,
                                  textvariable=self.combo_val)
        self.font_combo.grid(row=7, column=1, sticky='W', padx=(0,10))

        ## Label
        self.fontsize_label = ttk.Label(self.root, text='Size: ', font=('Helvetica', 18), justify='left')
        self.fontsize_label.grid(row=7, column=2, sticky='W')

        ## Entry
        self.fontsize_entry = ttk.Entry(self.root,
                                        font=18,
                                        width=5,
                                        validatecommand=self.entry_is_numeric,
                                        validate='all',
                                        textvariable=self.fontsize_val)
        self.fontsize_entry.grid(row=7, column=3, sticky='WE', pady=10)

        # status label
        self.status_label = ttk.Label(self.root, text="", justify='center')
        self.status_label.grid(row=8, column=1, columnspan=2, pady=15, sticky="WE")

        # submit button
        self.submit_button = ttk.Button(self.root, text='Submit', width=20,
        #                                 command=add_watermark(
        #     image_path=self.input_file_val.get(),
        #     output_path=self.output_dir_val.get(),
        #     watermark_text=self.watermark_text_val.get(),
        #     font_style=self.combo_val.get(),
        #     font_size=int(self.fontsize_val.get()),
        # )
                                        )
        self.submit_button.grid(row=9, column=1, columnspan=2, pady=15)

        self.root.mainloop()

    def input_browse_func(self):
            filename = tk.filedialog.askopenfilename(filetypes=(("jpeg files",".jpeg .jpg"), ("png files", ".png"), ("All files","*.*")))
            self.input_file_entry.insert(tk.END, filename)
            self.output_file_entry.insert(tk.END, self.get_file_dir())

    def get_file_dir(self):
        dir_str_list = self.input_file_entry.get().split('/')
        return "/".join(dir_str_list[:-1])

    def output_browse_func(self):
            dirname = tk.filedialog.askdirectory(initialdir=self.get_file_dir())
            self.output_file_entry.insert(tk.END, dirname)

    def entry_is_numeric(self):
        fontsize = self.fontsize_entry.get()
        if len(fontsize) == 0:
            self.status_label.configure(text="")
            return True
        elif fontsize.isnumeric():
            self.status_label.configure(text="")
            return True
        else:
            self.status_label.configure(text='The fontsize must be a number!')
            return False

if __name__ == '__main__':
    gui = WatermarkGUI()
    print(gui.combo_val.get())
