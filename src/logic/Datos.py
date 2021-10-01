from io import TextIOWrapper
from src.logic.Usuario import Usuario
from src.logic.Partida import Partida
import os
import csv

class Datos:
    def __init__(self, usuario : Usuario, partida : Partida) -> None:
        self._usuario = usuario
        self._partida = partida

    def crearArchivo (self) -> TextIOWrapper:
        archivo = open (os.path.join(os.getcwd(), 'src', 'files', 'partidas.csv'), 'w', encoding='UTF-8')
        writer = csv.writer(archivo)
        writer.writerow(["Usuario.nombre", "Usuario.axies", "Estado", "Slp", "Copas", "Fecha"])
        return archivo

    def guardar_datos(self):
        try:
            archivo = open (os.path.join(os.getcwd(), 'src', 'files', 'partidas.csv'), 'r+', encoding='UTF-8')
            archivo .seek(0,2)
        except FileNotFoundError:
            self.crearArchivo()
        
        datos_partida = [self._usuario.nombre(), self._usuario.axies(), self._partida.estado(), self._partida.slp(), self._partida.copas(), self._partida.fecha()]
        writer = csv.writer
        writer.writerows(datos_partida)
        archivo.close()