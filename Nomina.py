from abc import ABC, abstractmethod
from ast import Dict

from abc import ABC, abstractmethod
from datetime import datetime
from typing import List, Dict   


class cuentabancaria (ABC):
    def __init__(self, numero_cuenta: str, titular: str, saldo: float = 0):
        self.numero_cuenta = numero_cuenta
        self.titular = titular
        self.saldo = saldo
        self.historial_movimientos = list[Dict] = []

    @abstractmethod
    def calcular_comision(self, monto: float) -> float:
        """Metodo Abstracto: Cada tipo de cuenta tiene su propia comisión"""
        pass

    @abstractmethod
    def get_tipo_cuenta(self) -> str:
        """Metodo Abstracto: Returna el tipo de cuenta (Polimorfismo)"""
        pass

    def depositar(self, monto: float) -> bool:
        "Metodo heredado por todas las otras cuentas"
        if monto > 0:
            self._saldo += monto
            self._registrar_transaccion("DEPOSITO", monto)
            return True
        return False

    def retirar(self, monto: float) -> bool:
        "Metodo heredado por todas las otras cuentas"
        comision = self.calcular_comision(monto)
        total_retiro = monto + comision

        if total_retiro <= self._saldo:
            self._saldo -= total_retiro
            self._registrar_transaccion("RETIRO", monto, f"Comisión: {comision:,.0f}")
            return True
        return False