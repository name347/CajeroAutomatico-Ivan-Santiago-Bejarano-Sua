from abc import ABC, abstractmethod
from ast import Dict


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