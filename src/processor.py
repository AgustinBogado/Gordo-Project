import pandas as pd
import pdfplumber
from docx import Document


def read_word_table(path: str, key_col: str = "Producto") -> pd.DataFrame:
    """Lee la primera tabla del Word y devuelve un DataFrame."""
    doc = Document(path)
    table = doc.tables[0]
    rows = [[c.text.strip() for c in r.cells] for r in table.rows]
    return pd.DataFrame(rows[1:], columns=rows[0])


def read_excel(path: str) -> pd.DataFrame:
    """Lee un Excel y devuelve un DataFrame."""
    return pd.read_excel(path)


def diff_products(
    base_df: pd.DataFrame,
    new_df: pd.DataFrame,
    key_col: str = "Producto",
    price_col: str = "Precio",
):
    """Compara productos entre dos DataFrames."""

    base_ids = set(base_df[key_col])
    new_ids = set(new_df[key_col])

    to_add = sorted(new_ids - base_ids)
    to_remove = sorted(base_ids - new_ids)

    comunes = base_ids & new_ids
    to_update = {}
    for pid in comunes:
        old = base_df.loc[base_df[key_col] == pid, price_col].iloc[0]
        new = new_df.loc[new_df[key_col] == pid, price_col].iloc[0]
        if old != new:
            to_update[pid] = (old, new)

    return to_add, to_remove, to_update


def write_report(
    to_add: list[str],
    to_remove: list[str],
    to_update: dict[str, tuple[float, float]],
    path: str,
):
    """Escribe el informe de cambios en un .txt."""

    with open(path, "w", encoding="utf-8") as f:
        f.write("=== Productos a AGREGAR ===\n")
        for p in to_add:
            f.write(f"- {p}\n")
        f.write("\n=== Productos a ELIMINAR ===\n")
        for p in to_remove:
            f.write(f"- {p}\n")
        f.write("\n=== Precios ACTUALIZADOS ===\n")
        for p, (old, new) in to_update.items():
            f.write(f"- {p}: {old} → {new}\n")


def read_pdf(file_path):
    """Lee un archivo PDF y extrae texto de cada página."""
    with pdfplumber.open(file_path) as pdf:
        text = "\n".join(
            [page.extract_text() for page in pdf.pages if page.extract_text()]
        )
    return text
