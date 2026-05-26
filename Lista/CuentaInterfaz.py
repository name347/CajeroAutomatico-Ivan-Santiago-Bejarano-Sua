"""
🏦 CAJERO AUTOMÁTICO - Versión con POO
Autor: [XXXXXX]
Fecha: 2026
Características: Herencia, Polimorfismo, Encapsulamiento, Abstracción
"""

from abc import ABC, abstractmethod
from datetime import datetime
from typing import List, Dict

# =======================================================
# 1. CLASE BASE (CÓDIGO DE TU PROFESOR)
# =======================================================
class CuentaBancaria(ABC):
    """Clase abstracta que define el contrato para todas las cuentas."""

    def __init__(self, numero_cuenta: str, titular: str, saldo: float = 0):
        self._numero_cuenta = numero_cuenta  # Encapsulamiento
        self._titular = titular
        self._saldo = saldo
        self._historial: List[Dict] = []

    @abstractmethod
    def calcular_comision(self, monto: float) -> float:
        """Método abstracto: cada tipo de cuenta tiene su propia comisión."""
        pass

    @abstractmethod
    def get_tipo_cuenta(self) -> str:
        """Retorna el tipo de cuenta (polimorfismo)."""
        pass

    def depositar(self, monto: float) -> bool:
        """Método concreto heredado por todas las cuentas."""
        if monto > 0:
            self._saldo += monto
            self._registrar_transaccion("DEPÓSITO", monto)
            return True
        return False

    def retirar(self, monto: float) -> bool:
        """Método que puede ser sobrescrito (polimorfismo)."""
        comision = self.calcular_comision(monto)
        total_a_restar = monto + comision

        if total_a_restar <= self._saldo:
            self._saldo -= total_a_restar
            self._registrar_transaccion("RETIRO", -monto, f"Comisión: ${comision:,.0f}")
            return True
        return False

    def _registrar_transaccion(self, tipo: str, monto: float, detalle: str = ""):
        """Método protegido para registrar transacciones."""
        self._historial.append(
            {"fecha": datetime.now(), "tipo": tipo, "monto": monto, "detalle": detalle}
        )

    # Getters y Setters (Encapsulamiento)
    @property
    def saldo(self) -> float:
        return self._saldo

    @property
    def numero_cuenta(self) -> str:
        return self._numero_cuenta

    def get_historial(self) -> List[Dict]:
        return self._historial.copy()


# =======================================================
# 2. CLASES HIJAS (HERENCIA Y POLIMORFISMO)
# =======================================================
class CuentaAhorros(CuentaBancaria):
    """Cuenta con comisión fija por retiro."""
    
    def calcular_comision(self, monto: float) -> float:
        return 2000.0  # Comisión fija de $2,000 por cada retiro

    def get_tipo_cuenta(self) -> str:
        return "Cuenta de Ahorros"


class CuentaCorriente(CuentaBancaria):
    """Cuenta con comisión porcentual por retiro."""
    
    def calcular_comision(self, monto: float) -> float:
        return monto * 0.04  # Cobra el 4% del monto a retirar

    def get_tipo_cuenta(self) -> str:
        return "Cuenta Corriente"


# =======================================================
# 3. MENÚ DE INTERACCIÓN PRINCIPAL
# =======================================================
if __name__ == "__main__":
    # Creamos una cuenta de ahorros de prueba con $100,000 pesos
    cuenta = CuentaAhorros("12345", "Juan Pérez", 100000.0)
    
    while True:
        print("\n" + "="*30)
        print(f" 🏦 CAJERO AUTOMÁTICO - {cuenta.get_tipo_cuenta()}")
        print("="*30)
        print(f"Titular: {cuenta._titular}")
        print("1. Consultar Saldo")
        print("2. Depositar Dinero")
        print("3. Retirar Dinero")
        print("4. Ver Historial de Movimientos")
        print("5. Salir")
        
        opcion = input("Seleccione una opción (1-5): ")
        
        if opcion == "1":
            print(f"\n💰 Su saldo actual es: ${cuenta.saldo:,.0f}")
            
        elif opcion == "2":
            monto = float(input("\n💵 Ingrese el monto a depositar: "))
            if cuenta.depositar(monto):
                print("✅ Depósito exitoso.")
            else:
                print("❌ Monto inválido.")
                
        elif opcion == "3":
            monto = float(input("\n💸 Ingrese el monto a retirar: "))
            comision_estimada = cuenta.calcular_comision(monto)
            print(f"⚠️ Este retiro genera una comisión de: ${comision_estimada:,.0f}")
            
            if cuenta.retirar(monto):
                print("✅ Retiro exitoso. Retire su dinero.")
            else:
                print("❌ Saldo insuficiente (recuerde incluir la comisión).")
                
        elif opcion == "4":
            print("\n📜 HISTORIAL DE MOVIMIENTOS:")
            historial = cuenta.get_historial()
            if not historial:
                print("No hay movimientos registrados.")
            for transaccion in historial:
                fecha_str = transaccion["fecha"].strftime("%Y-%m-%d %H:%M:%S")
                print(f"[{fecha_str}] {transaccion['tipo']}: ${transaccion['monto']:,.0f} {transaccion['detalle']}")
                
        elif opcion == "5":
            print("\n👋 Gracias por usar nuestro cajero. ¡Hasta luego!")
            break
        else:
            print("❌ Opción no válida. Intente de nuevo.")