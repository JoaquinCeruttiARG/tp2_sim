import tkinter as tk
import distribuciones


def mostrarCampoCant_Muestras(ventana):
    p1_label = tk.Label(ventana, text="Tamaño de muesta:")
    p1_entry = tk.Entry(ventana)
    p1_label.grid(row=0, column=0, padx=10, pady=5)
    p1_entry.grid(row=0, column=1, padx=10, pady=5)
    return p1_entry


def mostrarListaIntervalos(ventana):
    p2_valores = ["10", "12", "16", "23"]
    p2_var = tk.StringVar(ventana)
    p2_var.set(p2_valores[0])

    p2_label = tk.Label(ventana, text="Cant_Intervalos:")
    p2_menu = tk.OptionMenu(ventana, p2_var, *p2_valores)

    p2_label.grid(row=1, column=0, padx=10, pady=5)
    p2_menu.grid(row=1, column=1, padx=10, pady=5)
    return p2_var


def uniforme():
    def graficarUniforme():
        muestras = pMuestras.get()
        intervalos = pIntervalos.get()
        a = pA_entry.get()
        b = pB_entry.get()
        distribuciones.generarArchivo("aleatorios.txt", muestras)
        distribuciones.uniforme("aleatorios.txt", a, b)
        distribuciones.graficar("DistUniforme.txt", intervalos)

    ventana = tk.Tk()
    ventana.title("Distribucion Uniforme")

    pA_label = tk.Label(ventana, text="A:")
    pA_entry = tk.Entry(ventana)

    pB_label = tk.Label(ventana, text="B:")
    pB_entry = tk.Entry(ventana)

    pIntervalos = mostrarListaIntervalos(ventana)
    pMuestras = mostrarCampoCant_Muestras(ventana)

    graficar_button = tk.Button(ventana, text="Graficar", command=graficarUniforme)

    pA_label.grid(row=2, column=0, padx=10, pady=5)
    pA_entry.grid(row=2, column=1, padx=10, pady=5)
    pB_label.grid(row=3, column=0, padx=10, pady=5)
    pB_entry.grid(row=3, column=1, padx=10, pady=5)
    graficar_button.grid(row=4, column=2, columnspan=2, padx=10, pady=10)


def normal():
    def graficarNormal():
        # Implementa la lógica de la Función 2 aquí
        muestras = pMuestras.get()
        intervalos = pIntervalos.get()
        a = p3_entry.get()
        b = p4_entry.get()
        distribuciones.generarArchivo("aleatorios.txt", muestras)
        distribuciones.boxMoller("aleatorios.txt", a, b)
        distribuciones.graficar("DistNormal.txt", intervalos)

    ventana = tk.Tk()
    ventana.title("Distribucion Normal")

    p3_label = tk.Label(ventana, text="Sigma:")
    p3_entry = tk.Entry(ventana)

    p4_label = tk.Label(ventana, text="Media:")
    p4_entry = tk.Entry(ventana)

    p3_label.grid(row=2, column=0, padx=10, pady=5)
    p3_entry.grid(row=2, column=1, padx=10, pady=5)
    p4_label.grid(row=3, column=0, padx=10, pady=5)
    p4_entry.grid(row=3, column=1, padx=10, pady=5)

    graficar_button = tk.Button(ventana, text="Graficar", command=graficarNormal)
    graficar_button.grid(row=4, column=2, columnspan=2, padx=10, pady=10)

    pIntervalos = mostrarListaIntervalos(ventana)
    pMuestras = mostrarCampoCant_Muestras(ventana)


def exponencial():
    def graficarExponencial():
        muestras = pMuestras.get()
        intervalos = pIntervalos.get()
        a = p5_entry.get()
        distribuciones.generarArchivo("aleatorios.txt", muestras)
        distribuciones.dist_Exponencial("aleatorios.txt", a)
        distribuciones.graficar("DistExponencial.txt", intervalos)

    ventana = tk.Tk()
    ventana.title("Distribucion Exponancial")

    p5_label = tk.Label(ventana, text="Lambda:")
    p5_entry = tk.Entry(ventana)
    p5_label.grid(row=2, column=0, padx=10, pady=5)
    p5_entry.grid(row=2, column=1, padx=10, pady=5)

    graficar_button = tk.Button(ventana, text="Graficar", command=graficarExponencial)
    graficar_button.grid(row=4, column=2, columnspan=2, padx=10, pady=10)

    pIntervalos = mostrarListaIntervalos(ventana)
    pMuestras = mostrarCampoCant_Muestras(ventana)


# Crear ventana
ventana = tk.Tk()
ventana.title("Selector de Funciones")

# Crear widgets
uniforme_button = tk.Button(ventana, text="Uniforme", command=uniforme)
normal_button = tk.Button(ventana, text="Normal", command=normal)
exponencial_button = tk.Button(ventana, text="Exponencial", command=exponencial)

# Posicionar widgets en la ventana
uniforme_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)
normal_button.grid(row=4, column=2, columnspan=2, padx=10, pady=10)
exponencial_button.grid(row=4, column=4, columnspan=2, padx=10, pady=10)

# Iniciar bucle de la ventana
ventana.mainloop()
