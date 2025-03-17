# Gordo-Project
A ver si puedo ayudar el gordo

La idea de este proyecto es que pueda hacer un programa que ayude al gordo (mi primo)
a hacer mas facil y rapido su trabajo para poder tener más tiempo y descansar más su cabeza c;


Primero se creo el entorno virtual "env" con: python -m venv env
Se activo el entorno virtual con: source env/Scripts/activate; para desactivar es: deactivate

Instalando dependencias de: tkinter - requests - reportlab - pandas - pdfplumber
Comando para instalar: pip install tkinter requests reportlab pandas pdfplumber

Creado requirements.txt
Guarda las bibliotecas instaladas con sus versiones con el comando: pip freeze > requirements.txt
Para luego poder instalarlas cuando se ejecuta: pip install -r requirements.txt

Creados carpeta src y 3 archivos: app - generator - processor (todos .py)
Añadido logica basica para empezar

La app se ejecuta con: python app.py
Una prueba para processor se hace con: df = read_excel("data/lista_productos.xlsx")

PD: en python se comenta con #