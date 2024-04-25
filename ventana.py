import tkinter as tk


def ventana_principal():
    def seleccionar_distribucion(distribucion_seleccionada):
        if distribucion_seleccionada == "uniforme":
            label_media.grid_remove()
            entry_media.grid_remove()
            label_desviacion.grid_remove()
            entry_desviacion.grid_remove()
            label_lambda.grid_remove()
            entry_lambda.grid_remove()
            label_limites.grid()
            entry_inferior.grid()
            label_hasta.grid()
            entry_superior.grid()

            # Deseleccionar otros Checkbox
            c_normal.deselect()
            c_exponencial.deselect()
        elif distribucion_seleccionada == "normal":
            label_media.grid()
            entry_media.grid()
            label_desviacion.grid()
            entry_desviacion.grid()
            label_lambda.grid_remove()
            entry_lambda.grid_remove()
            label_limites.grid_remove()
            entry_inferior.grid_remove()
            label_hasta.grid_remove()
            entry_superior.grid_remove()

            # Deseleccionar otros Checkbox
            c_uniforme.deselect()
            c_exponencial.deselect()

        elif distribucion_seleccionada == "exponencial":
            label_media.grid_remove()
            entry_media.grid_remove()
            label_desviacion.grid_remove()
            entry_desviacion.grid_remove()
            label_lambda.grid()
            entry_lambda.grid()
            label_limites.grid_remove()
            entry_inferior.grid_remove()
            label_hasta.grid_remove()
            entry_superior.grid_remove()

            # Deseleccionar otros Checkbox
            c_uniforme.deselect()
            c_normal.deselect()

    # Ventana
    ventana = tk.Tk()

    ventana.title("Generador de Distribuciones Aleatorias")

    # Frame
    frame = tk.Frame(ventana, width=600, height=1000)
    frame.pack(padx=50, pady=50)

    # Eleccion distribucion
    label_dist = tk.Label(frame, text="Seleccione una distribución: ")
    label_dist.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)

    var_uniforme = tk.BooleanVar(value=True)
    c_uniforme = tk.Checkbutton(frame, text="Uniforme", command=lambda: seleccionar_distribucion("uniforme"),
                                variable=var_uniforme)
    c_uniforme.grid(row=0, column=1, padx=10, pady=10)

    c_normal = tk.Checkbutton(frame, text="Normal", command=lambda: seleccionar_distribucion("normal"))
    c_normal.grid(row=0, column=2, padx=10, pady=10)

    c_exponencial = tk.Checkbutton(frame, text="Exponencial", command=lambda: seleccionar_distribucion("exponencial"))
    c_exponencial.grid(row=0, column=3, padx=10, pady=10)

    # Tamaño muestra
    label_tamano = tk.Label(frame, text="Tamaño: ")
    label_tamano.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)

    entry_tamano = tk.Entry(frame, width=50)
    entry_tamano.grid(row=1, column=1, columnspan=3, padx=10, pady=10)

    # Limites (Para uniforme)
    label_limites = tk.Label(frame, text="Limites: ")
    label_limites.grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)

    entry_inferior = tk.Entry(frame, width=10)
    entry_inferior.grid(row=2, column=1, padx=10, pady=10)

    label_hasta = tk.Label(frame, text="hasta")
    label_hasta.grid(row=2, column=2, padx=10, pady=10)

    entry_superior = tk.Entry(frame, width=10)
    entry_superior.grid(row=2, column=3, padx=10, pady=10)

    # Media (Para Normal)
    label_media = tk.Label(frame, text="Media: ")
    label_media.grid(row=3, column=0, padx=10, pady=10, sticky=tk.W)
    label_media.grid_remove()

    entry_media = tk.Entry(frame, width=50)
    entry_media.grid(row=3, column=1, columnspan=3, padx=10, pady=10)
    entry_media.grid_remove()

    # Desviacion (Para Normal)
    label_desviacion = tk.Label(frame, text="Desviacion: ")
    label_desviacion.grid(row=4, column=0, padx=10, pady=10, sticky=tk.W)
    label_desviacion.grid_remove()

    entry_desviacion = tk.Entry(frame, width=50)
    entry_desviacion.grid(row=4, column=1, columnspan=3, padx=10, pady=10)
    entry_desviacion.grid_remove()

    # Lambda (Para Exponencial)
    label_lambda = tk.Label(frame, text="Lambda: ")
    label_lambda.grid(row=5, column=0, padx=10, pady=10, sticky=tk.W)
    label_lambda.grid_remove()

    entry_lambda = tk.Entry(frame, width=50)
    entry_lambda.grid(row=5, column=1, columnspan=3, padx=10, pady=10)
    entry_lambda.grid_remove()

    # Boton confirmar
    boton_1 = tk.Button(frame, text="Confirmar")
    boton_1.grid(row=6, column=0, columnspan=4, padx=15, pady=15)

    ventana.mainloop()


ventana_principal()