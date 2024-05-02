import tkinter as tk
import generadores as g
import visualizacion
import subprocess
import os
import tkinter.messagebox as messagebox
import pruebas_bondad


# Variable global para mantener el índice actual de la lista
indice_actual = 0


# Lista global donde se almacenan los valores generados
lista =[]


# Variable global para almacenar el valor del intervalo seleccionado
intervalo_seleccionado = 10


def ventana_principal():


    # Función De Checkbox Distribuciones ---------------------------------------------
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


    # Funcion de CheckBox Intervalos ---------------------------------------------
    def intervalo_seleccionado(var):
        global intervalo_seleccionado
        lista_intervalos = [10,12,16,23]

        if var.get():
            contador = -1
            for check_var in checkbox_vars:
                contador += 1
                if check_var != var:
                    check_var.set(False)
                else:
                    # Actualizar la variable de intervalo seleccionado
                    intervalo_seleccionado = lista_intervalos[contador]


    # Función de botón confirmar  ---------------------------------------------
    def confirmar():
        global lista, expected_freq
        global indice_actual
        global intervalo_seleccionado
        lam = 0

        # Variable donde se almacena el tipo de distribucion seleccionada
        distribucion_seleccionada = ""
        if var_uniforme.get():
            distribucion_seleccionada = "uniforme"
        elif var_normal.get():
            distribucion_seleccionada = "normal"
        elif var_exponencial.get():
            distribucion_seleccionada = "exponencial"
        else:
            messagebox.showinfo("Error", "Debe seleccionar una distribución.")
            return

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

        # Verificar si al menos un checkbox de intervalo está marcado
        if not any([var_10.get(), var_12.get(), var_16.get(), var_23.get()]):
            messagebox.showinfo("Error", "Debe seleccionar al menos un intervalo.")
            return  # No proceder si ningún intervalo está seleccionado

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

        # LLamada a función que gráfica y genera excel
        visualizacion.generar_y_visualizar(lista, intervalo_seleccionado)
        # Llamada a función que muestra el gráfico en ventana
        mostrar_imagen()

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


        cc, ct, ksc, kst = pruebas_bondad.prueba(lista, intervalo_seleccionado, distribucion_seleccionada, lam)
        texto_prueba = f"Chi-2 Calculado: {cc}\nChi-2 Tabulado: {ct}\nKS Calculado: {ksc}\nKS Tabulado: {kst}"

        # Activar el entry_pruebas y agregar el texto
        entry_pruebas.config(state="normal")
        entry_pruebas.delete("1.0", tk.END)  # Borra cualquier contenido anterior
        entry_pruebas.insert(tk.END, texto_prueba)
        entry_pruebas.config(state="disabled")


    # Función para mostrar la imagen generada ---------------------------------------------
    def mostrar_imagen():
        # Obtener la ruta absoluta del directorio actual y el nombre de la imagen
        ruta_absoluta = os.path.abspath("histograma.png")

        # Ejecuta el comando para abrir la imagen con el visor de imágenes predeterminado
        subprocess.Popen(["start", "", "/b",  ruta_absoluta], shell=True)  # Para sistemas Windows


    # Funciones para moverse en la lista de números generados ---------------------------------------------
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


    def mostrar_anteriores_numeros():
        global indice_actual
        global lista

        if indice_actual > 199:
            entry_generados.config(state="normal")
            entry_generados.delete("1.0", tk.END) #Borra cualquier contenido anterior
            for elemento in lista[indice_actual-200: indice_actual]:
                entry_generados.config(state="normal")
                entry_generados.insert(tk.END, str(elemento) + "\n")
            entry_generados.config(state="disabled")
            indice_actual -= 200


    # Funcion siguiente y anterior ---------------------------------------------
    def siguiente():
        mostrar_proximos_numeros()

    def anterior():
        mostrar_anteriores_numeros()


    # Ventana ---------------------------------------------
    ventana = tk.Tk()
    ventana.title("Generador de Distribuciones Aleatorias")


    # Frame ---------------------------------------------
    frame = tk.Frame(ventana, width=600, height=1000)
    frame.pack(padx=50, pady=50)

    label_dist = tk.Label(frame, text="Seleccione una distribución: ")
    label_dist.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)


    # CheckBox Distribuciones ---------------------------------------------
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


    # Tamaño ---------------------------------------------
    label_tamano = tk.Label(frame, text="Tamaño: ")
    label_tamano.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)

    entry_tamano = tk.Entry(frame, width=50)
    entry_tamano.grid(row=1, column=1, columnspan=3, padx=10, pady=10)


    # Limites ---------------------------------------------
    label_limites = tk.Label(frame, text="Limites: ")
    label_limites.grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)

    entry_inferior = tk.Entry(frame, width=10)
    entry_inferior.grid(row=2, column=1, padx=10, pady=10)

    label_hasta = tk.Label(frame, text="hasta")
    label_hasta.grid(row=2, column=2, padx=10, pady=10)

    entry_superior = tk.Entry(frame, width=10)
    entry_superior.grid(row=2, column=3, padx=10, pady=10)


    # Media ---------------------------------------------
    label_media = tk.Label(frame, text="Media: ")
    label_media.grid(row=3, column=0, padx=10, pady=10, sticky=tk.W)
    label_media.grid_remove()

    entry_media = tk.Entry(frame, width=50)
    entry_media.grid(row=3, column=1, columnspan=3, padx=10, pady=10)
    entry_media.grid_remove()


    # Desviacion ---------------------------------------------
    label_desviacion = tk.Label(frame, text="Desviacion: ")
    label_desviacion.grid(row=4, column=0, padx=10, pady=10, sticky=tk.W)
    label_desviacion.grid_remove()

    entry_desviacion = tk.Entry(frame, width=50)
    entry_desviacion.grid(row=4, column=1, columnspan=3, padx=10, pady=10)
    entry_desviacion.grid_remove()


    # Lambda ---------------------------------------------
    label_lambda = tk.Label(frame, text="Lambda: ")
    label_lambda.grid(row=5, column=0, padx=10, pady=10, sticky=tk.W)
    label_lambda.grid_remove()

    entry_lambda = tk.Entry(frame, width=50)
    entry_lambda.grid(row=5, column=1, columnspan=3, padx=10, pady=10)
    entry_lambda.grid_remove()


    # Intervalos  ---------------------------------------------
    label_int = tk.Label(frame, text="Intervalos: ")
    label_int.grid(row=6, column=0, padx=10, pady=10, sticky=tk.W)

    checkbox_vars = []

    var_10 = tk.BooleanVar(value=True)
    checkbox_vars.append(var_10)
    c_10 = tk.Checkbutton(frame, text="10", variable=var_10, command=lambda: intervalo_seleccionado(var_10))
    c_10.grid(row=6, column=1, padx=10, pady=10)

    var_12 = tk.BooleanVar()
    checkbox_vars.append(var_12)
    c_12 = tk.Checkbutton(frame, text="12", variable=var_12, command=lambda: intervalo_seleccionado(var_12))
    c_12.grid(row=6, column=2, padx=10, pady=10)

    var_16 = tk.BooleanVar()
    checkbox_vars.append(var_16)
    c_16 = tk.Checkbutton(frame, text="16", variable=var_16, command=lambda: intervalo_seleccionado(var_16))
    c_16.grid(row=6, column=3, padx=10, pady=10)

    var_23 = tk.BooleanVar()
    checkbox_vars.append(var_23)
    c_23 = tk.Checkbutton(frame, text="23", variable=var_23, command=lambda: intervalo_seleccionado(var_23))
    c_23.grid(row=6, column=4, padx=10, pady=10)


    # Boton Confirmar ---------------------------------------------
    boton_1 = tk.Button(frame, text="Confirmar", command=confirmar)
    boton_1.grid(row=7, column=0, columnspan=4, padx=(10, 0), pady=10, sticky=tk.W)


    # Numeros Generados ---------------------------------------------
    label_generados = tk.Label(frame, text="Números generados: ")
    label_generados.grid(row=8, column=0, padx=10, pady=10, sticky=tk.W)

    entry_generados = tk.Text(frame, width=50, height=10, state="disabled")
    entry_generados.grid(row=8, column=0, columnspan=3, padx=10, pady=10)

    boton_ant = tk.Button(frame, text="Anterior", command=anterior)
    boton_ant.grid(row=9, column=0, padx=(10, 0), pady=10, sticky=tk.W)

    boton_sig = tk.Button(frame, text="Siguiente", command=siguiente)
    boton_sig.grid(row=9, column=2)


    # Chi2 y KS ---------------------------------------------
    label_pruebas = tk.Label(frame, text="Pruebas de Bondad: ")
    label_pruebas.grid(row=10, column=0, padx=10, pady=10, sticky=tk.W)

    entry_pruebas = tk.Text(frame, width=50, height=5, state="disabled")
    entry_pruebas.grid(row=11, column=0, columnspan=3, padx=10, pady=10)

    ventana.mainloop()


ventana_principal()