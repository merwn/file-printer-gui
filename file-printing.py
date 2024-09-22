import os
import sys
import argparse
import configparser
import logging
from tkinter import filedialog, messagebox, ttk
import tkinter as tk
import win32print
import win32api
from PIL import Image, ImageWin
from docx2pdf import convert

# Configure logging
logging.basicConfig(filename='file_printer.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Load configuration
config = configparser.ConfigParser()
config.read('config.ini')

DEFAULT_FILE_PATH = config.get('DEFAULT', 'file_path', fallback=r"C:\path\to\your\default\file.pdf")

def get_printers():
    return [printer[2] for printer in win32print.EnumPrinters(2)]

def select_file():
    file_paths = filedialog.askopenfilenames(filetypes=[
        ("Supported files", "*.pdf;*.gif;*.jpg;*.png;*.docx"),
        ("PDF files", "*.pdf"),
        ("Image files", "*.gif;*.jpg;*.png"),
        ("Word documents", "*.docx")
    ])
    if file_paths:
        file_path_var.set(';'.join(file_paths))

def print_file(file_path, printer_name, copies=1, page_range=None):
    try:
        file_ext = os.path.splitext(file_path)[1].lower()
        
        if file_ext == '.docx':
            pdf_path = file_path.replace('.docx', '.pdf')
            convert(file_path, pdf_path)
            file_path = pdf_path
            file_ext = '.pdf'

        if file_ext == '.pdf':
            win32api.ShellExecute(0, "print", file_path, f'/d:"{printer_name}"', ".", 0)
        elif file_ext in ['.gif', '.jpg', '.png']:
            image = Image.open(file_path)
            hdc = win32print.OpenPrinter(printer_name)
            try:
                win32print.StartDoc(hdc, file_path)
                win32print.StartPage(hdc)
                dib = ImageWin.Dib(image)
                dib.draw(hdc, (0, 0, image.width, image.height))
                win32print.EndPage(hdc)
                win32print.EndDoc(hdc)
            finally:
                win32print.ClosePrinter(hdc)
        
        logging.info(f"Successfully sent {file_path} to printer {printer_name}")
        return True
    except Exception as e:
        logging.error(f"Error printing file {file_path}: {e}")
        return False

def batch_print():
    file_paths = file_path_var.get().split(';')
    printer_name = printer_var.get()
    copies = int(copies_var.get())
    page_range = page_range_var.get()

    for file_path in file_paths:
        if print_file(file_path, printer_name, copies, page_range):
            messagebox.showinfo("Success", f"Successfully sent {file_path} to printer")
        else:
            messagebox.showerror("Error", f"Error printing file: {file_path}")

def view_print_queue():
    printer_name = printer_var.get()
    jobs = win32print.EnumJobs(win32print.OpenPrinter(printer_name), 0, -1, 1)
    queue_window = tk.Toplevel(root)
    queue_window.title("Print Queue")
    queue_window.geometry("400x300")
    
    tree = ttk.Treeview(queue_window, columns=('ID', 'Document', 'Status'), show='headings')
    tree.heading('ID', text='Job ID')
    tree.heading('Document', text='Document Name')
    tree.heading('Status', text='Status')
    
    for job in jobs:
        tree.insert('', 'end', values=(job['JobId'], job['pDocument'], job['pStatus']))
    
    tree.pack(expand=True, fill='both')

# Create the main window
root = tk.Tk()
root.title("Enhanced File Printer")
root.geometry("500x300")
root.configure(bg='#f0f0f0')

# Variables
file_path_var = tk.StringVar(value=DEFAULT_FILE_PATH)
printer_var = tk.StringVar(value=win32print.GetDefaultPrinter())
copies_var = tk.StringVar(value="1")
page_range_var = tk.StringVar(value="")

# Styles
button_style = {'bg': '#4CAF50', 'fg': 'white', 'font': ('Arial', 10), 'relief': 'flat', 'padx': 10, 'pady': 5}
label_style = {'bg': '#f0f0f0', 'font': ('Arial', 10)}
entry_style = {'font': ('Arial', 10), 'relief': 'solid', 'bd': 1}

# File selection
tk.Label(root, text="File(s):", **label_style).grid(row=0, column=0, padx=10, pady=10, sticky="e")
tk.Entry(root, textvariable=file_path_var, width=40, **entry_style).grid(row=0, column=1, padx=10, pady=10, sticky="ew")
tk.Button(root, text="Browse", command=select_file, **button_style).grid(row=0, column=2, padx=10, pady=10)

# Printer selection
tk.Label(root, text="Printer:", **label_style).grid(row=1, column=0, padx=10, pady=10, sticky="e")
ttk.Combobox(root, textvariable=printer_var, values=get_printers()).grid(row=1, column=1, columnspan=2, padx=10, pady=10, sticky="ew")

# Print settings
tk.Label(root, text="Copies:", **label_style).grid(row=2, column=0, padx=10, pady=10, sticky="e")
tk.Entry(root, textvariable=copies_var, width=5, **entry_style).grid(row=2, column=1, padx=10, pady=10, sticky="w")

tk.Label(root, text="Page Range:", **label_style).grid(row=3, column=0, padx=10, pady=10, sticky="e")
tk.Entry(root, textvariable=page_range_var, width=15, **entry_style).grid(row=3, column=1, padx=10, pady=10, sticky="w")

# Print button
print_button = tk.Button(root, text="PRINT", command=batch_print, **button_style)
print_button.grid(row=4, column=0, columnspan=3, sticky="ew", padx=10, pady=(20, 10))
print_button.configure(bg='#2196F3', font=('Arial', 12, 'bold'))

# Queue management
queue_button = tk.Button(root, text="View Print Queue", command=view_print_queue, **button_style)
queue_button.grid(row=5, column=0, columnspan=3, sticky="ew", padx=10, pady=10)

# Configure grid
root.grid_columnconfigure(1, weight=1)
for i in range(6):
    root.grid_rowconfigure(i, weight=1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Print files from command line or GUI.")
    parser.add_argument("files", nargs="*", help="Files to print")
    parser.add_argument("--printer", help="Printer to use")
    parser.add_argument("--copies", type=int, default=1, help="Number of copies")
    parser.add_argument("--page-range", help="Page range to print")
    
    args = parser.parse_args()
    
    if args.files:
        for file in args.files:
            if print_file(file, args.printer or win32print.GetDefaultPrinter(), args.copies, args.page_range):
                print(f"Successfully printed {file}")
            else:
                print(f"Failed to print {file}")
    else:
        root.mainloop()
