class Disco:

    def __init__(self, seekTime, velocidadRotacion, tiempoTransferenciaUnSector, tamañoBloque, totalPistas, posicionCabeza, sentido):
        self.seekTime = seekTime
        self.velocidadRotacion = velocidadRotacion
        self.tiempoTransferenciaUnSector = tiempoTransferenciaUnSector
        self.tamañoBloque = tamañoBloque
        self.totalPistas = totalPistas
        self.posicionCabeza = posicionCabeza
        self.sentido = sentido #C = Creciente     D = Decreciente

    def __str__(self):
        return (self.sentido)


