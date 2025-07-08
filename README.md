# Gordo-Project
Welcome, the idea of this project it's to practice in Python and help my cousin in his work... if i can.

First have to create the **Virtual Enviroment**: python -m venv env
To activate the Virtual Enviroment: source env/Scripts/activate
To deactivate: deactivate

Dependencies **required**: tkinter - requests - reportlab - pandas - pdfplumber
Command to install dependencies: pip install -r requirements.txt
To save the actual dependencies: pip freeze > requirements.txt
To install the dependencies: pip install -r requirements.txt

Created the folders to use: app - generator - processor

To start the app: python src/app.py  #It's **python** + the path of the app.py
To test processor: df = read_excel("data/lista_productos.xlsx")

Created "launcher.py" to modifi freely the launcher of the app.
Now app.py only have the call of the class "app".

## Nueva funcionalidad

La ventana inicial permite seleccionar:

1. **Lista Modificados**: archivo Excel con los precios nuevos.
2. **Lista Vieja**: lista PDF antigua generada con `create_pdf`.
3. **Carpeta de salida**: ubicación donde se guardará el resultado.

Al pulsar **Generar Lista** se crea un PDF con el nombre
`Lista Semanal Distribuidora Brown dd-mm-aaaa.pdf` dentro de la carpeta
seleccionada. También se genera un segundo PDF llamado
`No encontrados dd-mm-aaaa.pdf` con los productos que no se pudieron
actualizar.
