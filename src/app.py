import tkinter as tk
from tkinter import filedialog
from processor import read_excel, read_pdf
from generator import create_pdf

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx"), ("PDF files", "*.pdf")])
    if file_path:
        if file_path.endswith(".xlsx"):
            data = read_excel(file_path)
            print(data)
            create_pdf(data.to_dict(orient='records'), "output/lista_productos.pdf")
        elif file_path.endswith(".pdf"):
            text = read_pdf(file_path)
            print(text[:500])

# Crear ventana
root = tk.Tk()
root.title("Lector de Listas")

btn_open = tk.Button(root, text="Cargar Archivo", command=open_file)
btn_open.pack(pady=20)

root.mainloop()
