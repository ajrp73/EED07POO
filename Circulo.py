class Circulo:
    __slots__ = ['cx', '_cy', '__radio']

    def __init__(self, cx=None, cy=None, radio=None):
        if cx is None and cy is None and radio is None:
            self.cx= self._cy= 0 
            self.__radio= 1.0 
        else:
            self.cx= cx
            self._cy= cy
            self.__radio= radio
    
    def getCx(self):
        return self.cx

    def getCy(self):
        return self._cy
    
    def getRadio(self):
        return self.__radio

    def setCx(self, cx=10):
        if cx is None or not isinstance(cx, int):
            cx=0
        self.cx= cx
   
    def setCy(self, cy=None):
        if cy is None or cy is not isinstance(cy, int):
            self._cy=0
        else:
            self._cy= cy
    
    def setRadio(self, radio):
        if radio is None or not isinstance(radio, float):
            self.__radio=1.0
        else:
            self.__radio= radio
    
    #Devuelve una representación textual del objeto
    def toString(self):
        return f"({self.cx} {self.getCy()} {self.getRadio()})" 
        #A partir de la definición de métodos, se recomienda utilizarlos


class CirculoColor(Circulo):
    __slots__ = ['color']
    def __init__(self, cx=None, cy=None, radio=None, color=None):
        super().__init__(cx, cy, radio)
        if color is None:
            self.color= "blanco"
        else:
            self.color= color
    
    def toString(self):
        return f"({super().toString()} {self.color})"



c0=Circulo()
print("c0:", c0.toString())

c1=Circulo(2, 2, 2.0)
print("c1:", c1.toString())
c1._cy=44
c1.cx='hola'
print("c1:", c1.toString())
c1.setCy()
print("c1:", c1.toString())
print("c1:", c1.toString())

print("c1:", c1.toString())
c1.setRadio(2.5)
print("c1:", c1.toString())

print("c1:", c1.toString())
c1._cy='hola'
print("c1:", c1.toString())
try:
    c1.__radio=22.52
except:
    print("No es posible modificar directamente __radio porque es privado")

c1.setRadio(22.52)
print("c1:", c1.toString())

cc1= CirculoColor(8, 8, 8.0, "azul")
print("cc1:", cc1.toString())
