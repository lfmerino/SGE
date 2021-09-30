from typing import TYPE_CHECKING


class usuario:

    def test_Nombre(self,l):
        lmin = 6
        lmax = 12
        
        cont=1
        if len(l)<6: # Usuario al menos de 6 caracteres de longitud
            print("El nombre se usuario debe contener al menos 6 caracteres")
            return 1
        elif len(l)>12: # Usuario de no más de 12 caracteres de longitud
            print("El nombre de usuario no puede tener más de 12 caractéres")
            return 2
        elif not(l.isalnum()): # Usuario debe ser una cadena alfanumérica
            print("El nombre de usuario sólo puede contener caracteres alfanuméricos")
            return 3
        else: # Nombre se usuario correcto
            print("Nombre de usuario válido")
            return 0

    def test_passwd(self,p):
        numcar = may = min = dig = noalfnum = False
        esp = False
        lmin = 7

        if len(p) > lmin:
            numcar = True
        for c in p:
            if c.isspace(): # Comprobamos si hay espacios
                esp = True
            if c.isupper(): # Comprobamos si hay mayúsculas
                may = True
            if c.islower(): # Comprobamos si hay minúsculas
                min = True
            if c.isdigit(): # Comprobamos si hay números
                dig = True
            if not c.isalnum():
                noalfnum = True
        
        if (numcar and not esp and may and min and dig and noalfnum):
            return 0
        else:
            return 1


