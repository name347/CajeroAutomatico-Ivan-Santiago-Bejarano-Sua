import random

COLORES = ["green", "blue", "red", "purple", "orange", "darkblue", "magenta"]
ultimo_color = [None]

from tkinter import Tk, Toplevel, ttk

def enviar_texto(entrada):
    texto_ingresado = entrada.get()
    print(f"Texto enviado: {texto_ingresado}")

def abrir_opciones():
    ventana_opciones = Toplevel(root)
    ventana_opciones.title("Opciones adicionales")
    ventana_opciones.geometry("200x150")

    lbl_opc = ttk.Label(ventana_opciones, text="Configuración avanzada")
    lbl_opc.pack(pady=10)

    def ejecutar_accion_1():
        lbl_opc.config(text="¡Opción 1 Activada!", foreground="green")
        colores_disponibles = [c for c in COLORES if c != ultimo_color[0]]

        nuevo_color = random.choice(colores_disponibles)

        lbl_opc.config(text="¡Color Cambiado!", foreground=nuevo_color)

        ultimo_color[0] = nuevo_color

    btn_opc1 = ttk.Button(
        ventana_opciones, text="Opción 1", command=ejecutar_accion_1
    )

    btn_opc1 = ttk.Button(
        ventana_opciones, text="Opción 1", command=ejecutar_accion_1
    )
    btn_opc1.pack(pady=5)

def abrir_opciones():
    ventana_opciones = Toplevel(root)
    ventana_opciones.title("Información")
    ventana_opciones.geometry("200x150")

    lbl_opc = ttk.Label(ventana_opciones, text="Mas información sobre el programa")
    lbl_opc.pack(pady=10)

    entrada_texto = ttk.Entry(ventana_opciones, width=25)
    entrada_texto.pack(pady=5)

    btn_enviar = ttk.Button(
        ventana_opciones,
        text="Enviar",
        command=lambda: enviar_texto(entrada_texto),
    )
    btn_enviar.pack(pady=10)

if __name__ == "__main__":
    root = Tk()
    root.title("Mi aplicación")

    frm = ttk.Frame(root, padding=10)
    frm.grid()

    lbl = ttk.Label(frm, text="Ventana Python - ")
    lbl.grid(column=0, row=0)

    btn = ttk.Button(frm, text="Salir", command=root.destroy)
    btn.grid(column=1, row=0)

    btn = ttk.Button(frm, text="Cambiar color", command=abrir_opciones)
    btn.grid(column=2, row=0)

    btn = ttk.Button(frm, text="Escribir", command=abrir_opciones)
    btn.grid(column=3, row=0)

    root.mainloop()
