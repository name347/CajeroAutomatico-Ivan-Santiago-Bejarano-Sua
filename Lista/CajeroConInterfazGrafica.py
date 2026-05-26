""" CAJERO AUTOMÁTICO - Versión con POO y Tkinter Básico """

from abc import ABC, abstractmethod
from datetime import datetime
from typing import List, Dict
import tkinter as tk
from tkinter import messagebox

class CuentaBancaria(ABC):
    def __init__(self, numero_cuenta: str, titular: str, saldo: float = 0):
        self._numero_cuenta = numero_cuenta
        self._titular = titular
        self._saldo = saldo
        self._historial: List[Dict] = []

    @abstractmethod
    def calcular_comision(self, monto: float) -> float:
        pass

    @abstractmethod
    def get_tipo_cuenta(self) -> str:
        pass

    def depositar(self, monto: float) -> bool:
        if monto > 0:
            self._saldo += monto
            self._registrar_transaccion("DEPÓSITO", monto)
            return True
        return False

    def retirar(self, monto: float) -> bool:
        comision = self.calcular_comision(monto)
        total_a_restar = monto + comision

        if total_a_restar <= self._saldo:
            self._saldo -= total_a_restar
            self._registrar_transaccion("RETIRO", -monto, f"Comisión: ${comision:,.0f}")
            return True
        return False

    def _registrar_transaccion(self, tipo: str, monto: float, detalle: str = ""):
        self._historial.append(
            {"fecha": datetime.now(), "tipo": tipo, "monto": monto, "detalle": detalle}
        )

    @property
    def saldo(self) -> float:
        return self._saldo

    @property
    def numero_cuenta(self) -> str:
        return self._numero_cuenta

    def get_historial(self) -> List[Dict]:
        return self._historial.copy()

class CuentaAhorros(CuentaBancaria):
    def calcular_comision(self, monto: float) -> float:
        return 2000.0  

    def get_tipo_cuenta(self) -> str:
        return "Cuenta de Ahorros"

class CuentaCorriente(CuentaBancaria):
    def calcular_comision(self, monto: float) -> float:
        return monto * 0.04  

    def get_tipo_cuenta(self) -> str:
        return "Cuenta Corriente"

cuenta = CuentaAhorros("2809", "Ivan Santiago Bejarano Sua", 100000.0)

def actualizar_pantalla():
    """Esta función actualiza el texto del saldo en la ventana."""
    lbl_saldo.config(text=f"Saldo actual: ${cuenta.saldo:,.0f}")
    txt_monto.delete(0, tk.END)

def hacer_deposito():
    try:
        monto = float(txt_monto.get())
        if cuenta.depositar(monto):
            messagebox.showinfo("Éxito", "Dinero depositado correctamente.")
            actualizar_pantalla()
        else:
            messagebox.showerror("Error", "Monto no válido.")
    except ValueError:
        messagebox.showerror("Error", "Por favor ingresa un número válido.")

def hacer_retiro():
    try:
        monto = float(txt_monto.get())
        comision = cuenta.calcular_comision(monto)
        
        print(f"Retiro de ${monto} genera comisión de ${comision}")
        
        if cuenta.retirar(monto):
            messagebox.showinfo("Éxito", f"Retiro exitoso. Comisión cobrada: ${comision:,.0f}")
            actualizar_pantalla()
        else:
            messagebox.showerror("Error", "Saldo insuficiente (recuerde la comisión).")
    except ValueError:
        messagebox.showerror("Error", "Por favor ingresa un número válido.")

ventana = tk.Tk()
ventana.title("Cajero Automático")
ventana.geometry("225x250")

lbl_titulo = tk.Label(ventana, text="Cajero Automático", font=("Arial", 10,))
lbl_titulo.pack(pady=10)

lbl_usuario = tk.Label(ventana, text=f"Titular: {cuenta._titular}", font=("Arial", 10))
lbl_usuario.pack()

lbl_saldo = tk.Label(ventana, text="", font=("Arial", 10), fg="black")
lbl_saldo.pack(pady=10)

lbl_instruccion = tk.Label(ventana, text="Ingresa el monto:")
lbl_instruccion.pack()

txt_monto = tk.Entry(ventana, font=("Arial", 10), justify="center")
txt_monto.pack(pady=5)

btn_depositar = tk.Button(ventana, text="Depositar Dinero", command=hacer_deposito)
btn_depositar.pack(pady=5)

btn_retirar = tk.Button(ventana, text="Retirar Dinero", command=hacer_retiro)
btn_retirar.pack(pady=5)

actualizar_pantalla()

ventana.mainloop()