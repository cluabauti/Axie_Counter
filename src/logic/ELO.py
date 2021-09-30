class ELO:
    ELOS = {(0,799): 0, (800, 999): 1, (1000, 1099):3, (1100,1299):7, (1300, 1499): 8, (1500, 1799):9, (1800, 1999):10, (2000, 2199):11, (2200, 3000):12 }

    def __init__(self, elo) -> None:
        self._elo = elo

    @property
    def elo(self):
        return self._elo

    @elo.setter
    def elo (self, elo):
        self._elo = elo