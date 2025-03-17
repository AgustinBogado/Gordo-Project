import pandas as pd
import pdfplumber

def read_excel(file_path):
    """Lee un archivo Excel y extrae productos, precios y marcas."""
    df = pd.read_excel(file_path)
    print(df.head())  # Muestra las primeras filas para debug
    return df

def read_pdf(file_path):
    """Lee un archivo PDF y extrae texto de cada página."""
    with pdfplumber.open(file_path) as pdf:
        text = "\n".join([page.extract_text() for page in pdf.pages if page.extract_text()])
    print(text[:500])  # Muestra los primeros 500 caracteres para debug
    return text
