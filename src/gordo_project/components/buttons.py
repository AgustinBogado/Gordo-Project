import tkinter as tk

# Paleta de colores
colour1 = "#020f12"
colour2 = "#ff3939"
colour3 = "#ffffff"
colour4 = "black"

# Marco para los botones
button_frame = tk.Frame(
    self.main_frame,
    bg=colour1,
    highlightbackground=colour2,
    highlightthickness=2,
    bd=0,
    pady=20,
)
button_frame.grid(column=0, row=0)

btn_modificados = tk.Button(
    button_frame,
    text="Lista Modificados",
    bg=colour1,
    fg=colour2,
    activebackground=colour3,
    activeforeground=colour2,
    relief="flat",
    borderwidth=0,
    padx=20,
    pady=5,
    cursor="hand2",
    font=("Arial", 12, "bold"),
    command=self.load_excel,
)
btn_modificados.pack(pady=5)

btn_vieja = tk.Button(
    button_frame,
    text="Lista Vieja",
    bg=colour1,
    fg=colour2,
    activebackground=colour3,
    activeforeground=colour2,
    relief="flat",
    borderwidth=0,
    padx=20,
    pady=5,
    cursor="hand2",
    font=("Arial", 12, "bold"),
    command=self.load_pdf,
)
btn_vieja.pack(pady=5)

btn_dir = tk.Button(
    button_frame,
    text="Seleccionar Carpeta",
    bg=colour1,
    fg=colour2,
    activebackground=colour3,
    activeforeground=colour2,
    relief="flat",
    borderwidth=0,
    padx=20,
    pady=5,
    cursor="hand2",
    font=("Arial", 12, "bold"),
    command=self.select_output,
)
btn_dir.pack(pady=5)

btn_generate = tk.Button(
    button_frame,
    text="Generar Lista",
    bg=colour1,
    fg=colour2,
    activebackground=colour3,
    activeforeground=colour2,
    relief="flat",
    borderwidth=0,
    padx=20,
    pady=5,
    cursor="hand2",
    font=("Arial", 12, "bold"),
    command=self.generate,
)
btn_generate.pack(pady=5)