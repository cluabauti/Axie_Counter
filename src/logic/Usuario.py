from logic.ELO import ELO


class Usuario: 
    #Variables de instancia
    
    #Constructor
    def __init__ (self, elo: ELO, axies, slp: int = 0, copas: int = 0):
        self._slp = slp
        self._copas = copas
        self._elo = elo
        self.axies = axies
        self._partidas = 0 #aca tengo que inicializar las partidas en la clase partidas

    #Metodos
    def agregarSlp(self, cant : int):
        """Agrega la cantidad de slp pasada por parametro"""
        self._slp += cant

    def quitarSlp (self, cant : int):
        """Quita la cantidad de slp pasada por parametro"""
        self._slp += cant

    #def calcularElo (int copas)

    