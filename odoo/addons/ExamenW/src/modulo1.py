# -*- coding: utf-8 -*-
class Usuario1:
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
        
        


class Clave1:
    Salida=False
    MiNombre="C@mbiar21"
   
    __lmin = 8
       
    def test_nombre(self,nombre):
        if len(nombre)>=self.__lmin:
            if not any(letra.isspace() for letra in nombre):
                if any((letra<'0' or (letra>'9'and letra<'A') or letra>'z') for letra in nombre):
                    if any(letra.isdecimal() for letra in nombre):
                        if any(letra.islower() for letra in nombre):
                            if any(letra.isupper() for letra in nombre):
                                self.Salida=True
                                self.MiNombre = nombre
                               
                            else:
                                print("No mayúscula")
                        else:
                            print("No minúscula")
                    else:
                        print("No hay números")
                else:
                    print("No hay caracteres especiales")
            else:
                print("Hay espacios")
        else:
            
            print("Longitud")

 
                        
    def __init__(self,nombre):
        self.test_nombre(nombre)



class Usuario:
    Salida=False
    MiNombre="Usuario"
    __lmin = 6
    __lmax = 12
    
    def test_nombre(self,nombre):
        if (nombre.isalnum() and (self.__lmin > len(nombre)) and 
            (len(nombre) >= self.__lmax)): 
            self.MiNombre = nombre
            self.Salida=True
       
    
    def __init__(self,nombre):
        self.test_nombre(nombre)


class Clave:
    Salida=False
    MiNombre="C@mbiar21"
    __lmin = 8
       
    def test_nombre(self,nombre):
        if (len(nombre)>=self.__lmin and  not any(letra.isspace() for letra in nombre) and 
           any((letra<'0' or (letra>'9'and letra<'A') or letra>'z') for letra in nombre)
           and any(letra.isdecimal() for letra in nombre) and any(letra.islower() for letra in nombre) and 
           any(letra.isupper() for letra in nombre)):
           self.Salida=True
           self.MiNombre = nombre
                    

                        
    def __init__(self,nombre):
        self.test_nombre(nombre)


''' c =Clave1(input("Contraseña: "))
while not c.Salida:
    c.test_nombre(input("Contraseña: "))

print(c.MiNombre)'''




