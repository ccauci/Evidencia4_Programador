class Retroexcavadora:
    def __init__ (self, maxialtura, velocidadmaxi):
        self.alturamaxima = maxialtura
        self.velocidadmaxima = velocidadmaxi
        self.carga = 0
        self.posicion = 0
        
    def excavar (self, metros, tiempo):
        return metros / tiempo 
    
    def levantarcarga (self, carga, altura):
        if altura <= self.alturamaxima:
            self.cargaactual = carga
            return True
        return False
    
    def movimiento(self, velocidad, tiempo):
        if velocidad <= self.velocidadmaxima:
            self.posicion += velocidad * tiempo
            return self.posicion
        return "La velocidad excede el limite maximo"
    
    def __str__ (self):
        return f"La Retroexcavadora tiene una altura maxima {self.alturamaxima} y con una velocidad maxima {self.velocidadmaxima}"