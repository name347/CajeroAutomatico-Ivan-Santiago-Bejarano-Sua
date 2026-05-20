from tkinter import Tk, ttk

def saludar_usuario(entrada, etiqueta_resultado):
    nombre = entrada.get().strip()
    if nombre:
        etiqueta_resultado.config(text=f"Muy Buenas noches querid@, {nombre} sea Bienvenid@")
    else:
        etiqueta_resultado.config(text="Primero escribe tu nombre")

def limpiar_texto(entrada, etiqueta_resultado):
    entrada.delete(0, "end")
    etiqueta_resultado.config(text="")

if __name__ == "__main__":
    root = Tk()
    root.title("Saludador con Tkinter")

    frm = ttk.Frame(root, padding=20)
    frm.grid()

    lbl_bienvenida = ttk.Label(frm, text="Bienvenido a la aplicación de saludos")
    lbl_bienvenida.grid(column=0, row=0, columnspan=3, pady=10)

    lbl_instruccion = ttk.Label(frm, text="Escribe tu nombre:")
    lbl_instruccion.grid(column=0, row=1, pady=5)

    entrada_texto = ttk.Entry(frm, width=25)
    entrada_texto.grid(column=1, row=1, columnspan=2, pady=5)

    lbl_saludo = ttk.Label(frm, text="", font=("Arial", 10, "bold"))
    lbl_saludo.grid(column=0, row=4, columnspan=3, pady=15)

    btn_saludar = ttk.Button(
        frm,
        text="Saludar al usuario",
        command=lambda: saludar_usuario(entrada_texto, lbl_saludo),
    )
    btn_saludar.grid(column=0, row=2, padx=3)

    btn_limpiar = ttk.Button(
        frm,
        text="Limpiar Texto",
        command=lambda: limpiar_texto(entrada_texto, lbl_saludo),
    )
    btn_limpiar.grid(column=1, row=2, padx=3)

    btn_salir = ttk.Button(frm, text="Salir de la aplicación", command=root.destroy)
    btn_salir.grid(column=2, row=2, padx=3)

    root.mainloop()