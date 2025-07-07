import tkinter as tk
from tkinter import filedialog
from processor import read_excel, read_pdf
from generator import create_pdf

class App(tk.Tk):
    def __init__(self):
        super().__init__()  # <-- inicializa la ventana Tk
        self.geometry("350x300")
        self.resizable(False, False)
        self.title("Lector de Listas")

        # Paleta de colores
        colour1 = "#020f12"
        colour2 = "#ff3939"
        colour3 = "#ffffff"
        colour4 = "black"

        # Frame principal
        self.main_frame = tk.Frame(self, bg=colour1, pady=40)
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        self.main_frame.columnconfigure(0, weight=1)
        self.main_frame.rowconfigure(0, weight=1)

        borde_btn = tk.Frame(
            self.main_frame,
            bg=colour1,
            highlightbackground=colour2,
            highlightthickness=2,
            bd=0
        )
        borde_btn.grid(column=0, row=0, pady=20)

        # Botón “Cargar Archivo”
        btn_upload = tk.Button(
            borde_btn,
            text="Cargar Archivo",
            bg=colour1,
            fg=colour2,
            activebackground=colour3,
            activeforeground=colour2,
            relief="flat",
            borderwidth=0,
            padx=20,
            pady=8,
            cursor="hand2",
            font=("Arial", 16, "bold"),
            command=self.open_file
        )
        btn_upload.pack()

    def open_file(self):
        tipos = [
            ("Archivos Excel", "*.xlsx"),
            ("Archivos PDF",    "*.pdf"),
            ("Documentos Word","*.docx"),
            ("Todos los archivos", "*.*"),
        ]
        ruta = filedialog.askopenfilename(filetypes=tipos)
        if not ruta:
            return

        ruta_low = ruta.lower()
        if ruta_low.endswith(".xlsx"):
            df = read_excel(ruta)
            create_pdf(df.to_dict(orient="records"), "output/lista_productos.pdf")
        elif ruta_low.endswith(".pdf"):
            texto = read_pdf(ruta)
            print(texto[:500])
        elif ruta_low.endswith(".docx"):
            print("Word seleccionado:", ruta)

if __name__ == "__main__":
    app = App()
    app.mainloop()
