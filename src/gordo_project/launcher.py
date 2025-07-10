import os
import tkinter as tk
from tkinter import filedialog, messagebox
from datetime import datetime
from gordo_project.processor import (
    read_excel,
    parse_pdf_products,
    update_prices,
)
from gordo_project.components.buttons import (
    btn_path,
    btn_old_list,
    btn_list_modifieds,
    btn_generate,
)

class App(tk.Tk):
    def __init__(self):
        super().__init__()  # <-- inicializa la ventana Tk
        self.geometry("450x3400")
        self.resizable(False, False)
        self.title("Lector de Listas")

        self.modified_path = None
        self.old_pdf_path = None
        self.output_dir = None

        # Frame principal
        self.main_frame = tk.Frame(self, bg="#020f12", pady=40)
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        self.main_frame.columnconfigure(0, weight=1)
        self.main_frame.rowconfigure(0, weight=1)

    def load_excel(self):
        ruta = filedialog.askopenfilename(filetypes=[("Archivos Excel", "*.xlsx")])
        if ruta:
            self.modified_path = ruta

    def load_pdf(self):
        ruta = filedialog.askopenfilename(filetypes=[("Archivos PDF", "*.pdf")])
        if ruta:
            self.old_pdf_path = ruta

    def select_output(self):
        carpeta = filedialog.askdirectory()
        if carpeta:
            self.output_dir = carpeta

    def generate(self):
        if not (self.modified_path and self.old_pdf_path and self.output_dir):
            messagebox.showerror(
                "Error",
                "Debe seleccionar la lista de modificados, la lista vieja y la carpeta de destino.",
            )
            return

        df = read_excel(self.modified_path)
        modified_products = df.to_dict(orient="records")
        old_products = parse_pdf_products(self.old_pdf_path)
        updated, not_found = update_prices(old_products, modified_products)

        fecha = datetime.now().strftime("%d-%m-%Y")
        output_pdf = os.path.join(
            self.output_dir, f"Lista Semanal Distribuidora Brown {fecha}.pdf"
        )
        create_pdf(updated, output_pdf)

        if not_found:
            nf_pdf = os.path.join(self.output_dir, f"No encontrados {fecha}.pdf")
            create_pdf(not_found, nf_pdf)

        messagebox.showinfo("Proceso finalizado", "Listas generadas correctamente")

if __name__ == "__main__":
    app = App()
    app.mainloop()
