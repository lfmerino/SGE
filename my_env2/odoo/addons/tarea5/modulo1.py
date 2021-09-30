class Usuario:
    Salida=0
    MiNombre="Usuario"
    __lmin = 6
    __lmax = 12
    
    def test_nombre(self,nombre):
        if nombre.isalnum():
            if (self.__lmin > len(nombre)):
                self.Salida = 1
            elif (len(nombre) >= self.__lmax): 
                self.Salida = 2
            else:
                self.MiNombre = nombre        
        else:
            self.Salida = 3
    
    def __init__(self,nombre):
        self.test_nombre(nombre)
        




