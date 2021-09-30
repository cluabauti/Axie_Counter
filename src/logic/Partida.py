from datetime import date as Date
from time import sleep

class Partida:
    def __init__(self, estado, slp : int = 0, copas : int = 0, fecha : Date = Date.today()):
        self._estado = estado
        self._slp = slp
        self._copas = copas
        self._fecha = fecha

    #Getters y setters
    @property
    def slp (self) -> int:
        return self._slp

    @slp.setter
    def slp(self, slp):
        self._slp = slp

    @property
    def estado(self):
        return self._estado

    @estado.setter
    def estado(self, estado):
        self._estado = estado

    @property
    def copas(self):
        return self._copas

    @copas.setter
    def copas (self, copas):
        self._copas = copas

    @property
    def fecha(self):
        return self._fecha

    @fecha.setter
    def fecha(self, fecha):        
        self._fecha = fecha

    