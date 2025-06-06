from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os

def create_pdf(products, output_path):
    """Genera un PDF con la lista de productos y precios."""
    # Ensure the directory for the output exists to avoid FileNotFoundError
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    c = canvas.Canvas(output_path, pagesize=letter)
    width, height = letter
    
    y_position = height - 40  # Empezamos un poco abajo en la página
    
    for product in products:
        name = product['Producto']
        price = product['Precio']
        brand = product['Marca']
        
        c.drawString(40, y_position, f"Producto: {name}")
        c.drawString(40, y_position - 20, f"Precio: ${price}")
        c.drawString(40, y_position - 40, f"Marca: {brand}")
        
        y_position -= 60  # Espacio entre productos
        
        if y_position < 40:  # Si no hay espacio, agregar una nueva página
            c.showPage()
            y_position = height - 40
    
    c.save()

# Ejemplo de uso
if __name__ == "__main__":
    products = [
        {'Producto': 'Producto A', 'Precio': '100', 'Marca': 'Marca A'},
        {'Producto': 'Producto B', 'Precio': '200', 'Marca': 'Marca B'}
    ]
    create_pdf(products, "output/lista_productos.pdf")
