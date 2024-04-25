import tkinter as tk
import generadores as g

# Variable global para mantener el índice actual de la lista
indice_actual = 0

# Lista global donde se almacenan los valores generados
lista =[]

def ventana_principal():


    # Función De Checkbox
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

            c_uniforme.deselect()
            c_normal.deselect()

    # Función de botón confirmar
    def confirmar():
        global lista
        global indice_actual

        # Variable donde se almacena el tipo de distribucion seleccionada
        distribucion_seleccionada = ""
        if var_uniforme.get():
            distribucion_seleccionada = "uniforme"
        elif var_normal.get():
            distribucion_seleccionada = "normal"
        elif var_exponencial.get():
            distribucion_seleccionada = "exponencial"

        # Variable donde se almacena el tamaño de la muestra
        tamano_muestra = int(entry_tamano.get())

        # Obteniendo los datos de los campos de entrada y convirtiéndolos a float

        if distribucion_seleccionada == "normal":
            media = float(entry_media.get())
            desviacion = float(entry_desviacion.get())
        elif distribucion_seleccionada == "exponencial":
            lam = float(entry_lambda.get())
        elif distribucion_seleccionada == "uniforme":
            limite_inferior = int(entry_inferior.get())
            limite_superior = int(entry_superior.get())
        else:
            print("Debe seleccionar una distribución")

        # Llamada a los generadores
        if distribucion_seleccionada == "normal":
            if isinstance(media, (float, int)) and isinstance(desviacion, (float, int)):
                indice_actual = 0
                lista = g.generar_normal(media, desviacion, tamano_muestra)
        elif distribucion_seleccionada == "exponencial":
            if isinstance(lam, (float, int)):
                indice_actual = 0
                lista = g.generar_exponencial(lam, tamano_muestra)
        elif distribucion_seleccionada == "uniforme":
            if isinstance(limite_inferior, (float, int)) and isinstance(limite_superior, (float, int)):
                indice_actual = 0
                lista = g.generar_uniforme(limite_inferior, limite_superior, tamano_muestra)


        # Para ir chequeando en consola
        print("Distribución seleccionada:", distribucion_seleccionada)
        print("Tamaño de la muestra:", tamano_muestra)
        if distribucion_seleccionada == "normal":
            print("Media:", media)
            print("Desviación:", desviacion)
        if distribucion_seleccionada == "exponencial":
            print("Lambda:", lam)
        if distribucion_seleccionada == "uniforme":
            print("Límite Inferior:", limite_inferior)
            print("Límite Superior:", limite_superior)
        print(lista)

        # Verificar si la lista está vacía
        if len(lista) == 0:
            entry_generados.config(state="normal")
            entry_generados.delete("1.0", tk.END)  # Borra cualquier contenido anterior
            entry_generados.insert(tk.END, "Lista Vacía")
            entry_generados.config(state="disabled")
        else:
            # Imprimir los primeros 200 elementos de la lista en la entrada
            entry_generados.config(state="normal")
            entry_generados.delete("1.0", tk.END)  # Borra cualquier contenido anterior
            for elemento in lista[:200]:
                entry_generados.insert(tk.END, str(elemento) + "\n")
            entry_generados.config(state="disabled")


    # Funcion para moverse en la lista de números generados
    def mostrar_proximos_numeros():
        global indice_actual
        global lista


        if indice_actual < len(lista):
            entry_generados.config(state="normal")
            entry_generados.delete("1.0", tk.END)  # Borra cualquier contenido anterior
            for elemento in lista[indice_actual:indice_actual + 200]:
                entry_generados.config(state="normal")
                entry_generados.insert(tk.END, str(elemento) + "\n")
            entry_generados.config(state="disabled")
            indice_actual += 200

        # Pruebas
        print(indice_actual)
        print(len(lista))


    # Funcion siguiente
    def siguiente():
        mostrar_proximos_numeros()


    # Ventana
    ventana = tk.Tk()
    ventana.title("Generador de Distribuciones Aleatorias")


    # Frame
    frame = tk.Frame(ventana, width=600, height=1000)
    frame.pack(padx=50, pady=50)

    label_dist = tk.Label(frame, text="Seleccione una distribución: ")
    label_dist.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)


    # CheckBox
    var_uniforme = tk.BooleanVar(value=True)
    c_uniforme = tk.Checkbutton(frame, text="Uniforme", command=lambda: seleccionar_distribucion("uniforme"),
                                variable=var_uniforme)
    c_uniforme.grid(row=0, column=1, padx=10, pady=10)

    var_normal = tk.BooleanVar()
    c_normal = tk.Checkbutton(frame, text="Normal", command=lambda: seleccionar_distribucion("normal"),
                              variable=var_normal)
    c_normal.grid(row=0, column=2, padx=10, pady=10)

    var_exponencial = tk.BooleanVar()
    c_exponencial = tk.Checkbutton(frame, text="Exponencial", command=lambda: seleccionar_distribucion("exponencial"),
                                   variable=var_exponencial)
    c_exponencial.grid(row=0, column=3, padx=10, pady=10)


    # Tamaño
    label_tamano = tk.Label(frame, text="Tamaño: ")
    label_tamano.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)

    entry_tamano = tk.Entry(frame, width=50)
    entry_tamano.grid(row=1, column=1, columnspan=3, padx=10, pady=10)


    # Limites
    label_limites = tk.Label(frame, text="Limites: ")
    label_limites.grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)

    entry_inferior = tk.Entry(frame, width=10)
    entry_inferior.grid(row=2, column=1, padx=10, pady=10)

    label_hasta = tk.Label(frame, text="hasta")
    label_hasta.grid(row=2, column=2, padx=10, pady=10)

    entry_superior = tk.Entry(frame, width=10)
    entry_superior.grid(row=2, column=3, padx=10, pady=10)


    # Media
    label_media = tk.Label(frame, text="Media: ")
    label_media.grid(row=3, column=0, padx=10, pady=10, sticky=tk.W)
    label_media.grid_remove()

    entry_media = tk.Entry(frame, width=50)
    entry_media.grid(row=3, column=1, columnspan=3, padx=10, pady=10)
    entry_media.grid_remove()


    # Desviacion
    label_desviacion = tk.Label(frame, text="Desviacion: ")
    label_desviacion.grid(row=4, column=0, padx=10, pady=10, sticky=tk.W)
    label_desviacion.grid_remove()

    entry_desviacion = tk.Entry(frame, width=50)
    entry_desviacion.grid(row=4, column=1, columnspan=3, padx=10, pady=10)
    entry_desviacion.grid_remove()


    # Lambda
    label_lambda = tk.Label(frame, text="Lambda: ")
    label_lambda.grid(row=5, column=0, padx=10, pady=10, sticky=tk.W)
    label_lambda.grid_remove()

    entry_lambda = tk.Entry(frame, width=50)
    entry_lambda.grid(row=5, column=1, columnspan=3, padx=10, pady=10)
    entry_lambda.grid_remove()


    # Boton Confirmar
    boton_1 = tk.Button(frame, text="Confirmar", command=confirmar)
    boton_1.grid(row=6, column=0, columnspan=4, padx=(10, 0), pady=10, sticky=tk.W)


    # Numeros Generados
    label_generados = tk.Label(frame, text="Números generados: ")
    label_generados.grid(row=7, column=0, padx=10, pady=10, sticky=tk.W)

    entry_generados = tk.Text(frame, width=50, height=10, state="disabled")
    entry_generados.grid(row=8, column=0, columnspan=3, padx=10, pady=10)

    #boton_ant = tk.Button(frame, text="Anterior")
    #boton_ant.grid(row=9, column=0, padx=(10, 0), pady=10, sticky=tk.W)

    boton_sig = tk.Button(frame, text="Siguiente", command=siguiente)
    boton_sig.grid(row=9, column=2)

    ventana.mainloop()


ventana_principal()