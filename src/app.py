from tkinter import filedialog, messagebox, Tk, Button
from processor import read_word_table, read_excel, diff_products, write_report


def run_report():
    word_base = filedialog.askopenfilename(
        title="Word base (.docx)", filetypes=[("Word", "*.docx")]
    )
    if not word_base:
        return

    excel_nuevo = filedialog.askopenfilename(
        title="Excel nuevos (.xlsx)", filetypes=[("Excel", "*.xlsx")]
    )
    if not excel_nuevo:
        return

    base_df = read_word_table(word_base)
    new_df = read_excel(excel_nuevo)
    to_add, to_remove, to_update = diff_products(base_df, new_df)

    salida = filedialog.asksaveasfilename(
        title="Guardar informe (.txt)",
        defaultextension=".txt",
        filetypes=[("Text", "*.txt")],
    )
    if not salida:
        return

    write_report(to_add, to_remove, to_update, salida)
    messagebox.showinfo("Listo", f"Informe generado en:\n{salida}")


if __name__ == "__main__":
    root = Tk()
    root.title("Generar Informe de Cambios")
    btn = Button(root, text="Crear informe .txt", command=run_report)
    btn.pack(padx=20, pady=20)
    root.mainloop()
