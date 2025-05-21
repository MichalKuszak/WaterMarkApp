import tkinter as tk
from tkinter import filedialog
import ttkbootstrap as ttk
import pygubu
from ttkbootstrap import Style

from img_functions import watermark_text

root = tk.Tk()
root.config(padx=20, pady=20)
style = Style(theme='darkly')
root.title('Watermark')
# root.geometry('200x100')



# title
title_label = ttk.Label(root, text='Watermark your image', font=('Helvetica', 24))
title_label.grid(row=0, column=0, columnspan=4, padx=30, pady=(0, 30))

# select input directory
input_label = ttk.Label(root, text='Select image to overlay:', font=('Helvetica', 18), justify='left')
input_label.grid(row=1, column=0, columnspan=4, sticky='W')

input_file_entry = ttk.Entry(root, font=20)
input_file_entry.grid(row=2, column=0, columnspan=3, sticky='WE')

def input_browse_func():
    filename = tk.filedialog.askopenfilename(filetypes=(("jpeg files",".jpeg .jpg"), ("png files", ".png"), ("All files","*.*")))
    input_file_entry.insert(tk.END, filename)

input_file_button = ttk.Button(root, text="Browse", command=input_browse_func)
input_file_button.grid(row=2, column=3, sticky='WE', pady=10)

# select output directory
output_label = ttk.Label(root, text='Select path to save the image:', font=('Helvetica', 18), justify='left')
output_label.grid(row=3, column=0, columnspan=4, sticky='W')

output_file_entry = ttk.Entry(root, font=20)
output_file_entry.grid(row=4, column=0, columnspan=3, sticky='WE')

def output_browse_func():
    dirname = tk.filedialog.askdirectory()
    output_file_entry.insert(tk.END, dirname)

output_file_button = ttk.Button(root, text="Browse", command=output_browse_func)
output_file_button.grid(row=4, column=3, sticky='WE', pady=10)

# entry for watermark text
watermark_text_label = ttk.Label(root, text='Text to overlay: ', font=('Helvetica', 18), justify='left')
watermark_text_label.grid(row=5, column=0, columnspan=4, sticky='W')

watermark_text_entry = ttk.Entry(root, font=18)
watermark_text_entry.grid(row=6, column=0, columnspan=4, sticky='WE', pady=10)

# font and fontsize selection
fonttype_label = ttk.Label(root, text='Font: ', font=('Helvetica', 18), justify='left')
fonttype_label.grid(row=7, column=0, sticky='W')

font_combo = ttk.Combobox(root,
                          state='readonly',
                          values=['Helvetica',
                                  'Roboto',
                                  'Times New Roman',
                                  'Georgia',
                                  'Comic Sans',
                                  'Verdana',
                                  'Arial',
                                  'Garamond',
                                  'Baskerville',
                                  'Futura',
                                  'Bodoni',
                                  'Rockwell'],
                          width=15)
font_combo.grid(row=7, column=1, sticky='W', padx=(0,10))

fontsize_label = ttk.Label(root, text='Size: ', font=('Helvetica', 18), justify='left')
fontsize_label.grid(row=7, column=2, sticky='W')

fontsize_entry = ttk.Entry(root, font=18, width=5)
fontsize_entry.grid(row=7, column=3, sticky='WE', pady=10)


# submit button
submit_button = ttk.Button(root, text='Submit', width=20)
submit_button.grid(row=8, column=1, columnspan=2, pady=15)

root.mainloop()
