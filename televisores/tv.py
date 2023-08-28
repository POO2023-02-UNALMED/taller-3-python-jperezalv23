class TV:
    _numTV = 0
    def __init__(self, marca, estado):
        self.marca = marca
        self.estado = estado
        self.canal = 1
        self.volumen = 1
        self.precio = 500
        TV._numTV += 1

    def setMarca(self, marca):
        self.marca = marca
    
    def setCanal(self, canal):
        self.canal = canal

    def setPrecio(self, precio):
        self.precio = precio

    def setVolumen(self, volumen):
        self.volumen = volumen
    
    def setControl(self, control):
        self.control = control

    def getMarca(self):
        return self.marca
    
    def getCanal(self):
        return self.canal

    def getPrecio(self):
        return self.precio

    def getVolumen(self):
        return self.volumen
    
    def getControl(self):
        return self.control
    
    def setNumTV(self, numero):
        self.numTV = numero
    
    def getNumTV(self):
        return self.numTV
    
    def turnOn(self):
        self.estado = True

    def turnOff(self):
        self.estado = False

    def getEstado(self):
        return self.estado
    
    def canalUp(self):
        if self.canal >= 1 and self.canal < 120 and self.estado is True:
            self.canal += 1

    def canalDown(self):
        if self.canal > 1 and self.canal <= 120 and self.estado is True:
            self.canal -= 1

    def volumenUp(self):
        if self.volumen >= 0 and self.volumen < 7 and self.estado is True:
            self.volumen += 1

    def volumenDown(self):
        if self.volumen > 0 and self.volumen <= 7 and self.estado is True:
            self.volumen -= 1

    


        
    

    


    
