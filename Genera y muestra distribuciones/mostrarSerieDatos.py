import tkinter as tk
from tkinter import scrolledtext

def cargarSerieDatos(archivo):
    
    # Crear la ventana principal
    ventana = tk.Tk()
    ventana.title("Visualizador de Datos")

    # Crear un cuadro de texto con scroll
    texto = scrolledtext.ScrolledText(ventana, width=40, height=10, wrap=tk.WORD)
    texto.pack(padx=10, pady=10)

    # Botón para cargar datos
    boton_cargar = tk.Button(ventana, text="Cargar Datos", command=cargarSerieDatos)
    boton_cargar.pack(pady=5)

    # Botón para salir
    boton_salir = tk.Button(ventana, text="Salir", command=ventana.quit)
    boton_salir.pack(pady=5)
    
    # Cargar datos desde archivo
    try:
        with open(archivo, "r") as archivo:
            datos = archivo.read()
            texto.delete(1.0, tk.END)
            texto.insert(tk.END, datos)
    except FileNotFoundError:
        texto.delete(1.0, tk.END)
        texto.insert(tk.END, "Archivo no encontrado.")


    # Ejecutar la ventana
    ventana.mainloop()