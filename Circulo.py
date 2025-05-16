class Circulo:
    def __init__(self, cx=None, cy=None, radio=None):
        if cx is None and cy is None and radio is None:
            self.cx= self.cy= 0 
            self.radio= 1.0 
        else:
            self.cx= cx
            self.cy= cy
            self.radio= radio
    
    def getCx(self):
        return self.cx

    def getCy(self):
        return self.cy
    
    def getRadio(self):
        return self.radio

    def setCx(self, cx=10):
        if cx is None or not isinstance(cx, int):
            cx=0
        
        self.cx= cx
   
    def setCy(self, cy=None):
        if cy is None or cy is not isinstance(cy, int):
            self.cy=0
        else:
            self.cy= cy
    
    def setRadio(self, radio):
        if radio is None or not isinstance(radio, float):
            self.radio=1.0
        else:
            self.radio= radio
    
    #Devuelve una representación textual del objeto
    def toString(self):
        return f"({self.cx} {self.getCy()} {self.getRadio()})" 
        #A partir de la definición de métodos, se recomienda utilizarlos

c0=Circulo()
print("c0:", c0.toString())

c1=Circulo(2, 2, 2.0)
print("c1:", c1.toString())
c1.setCx()
print("c1:", c1.toString())
c1.setCy()
print("c1:", c1.toString())
