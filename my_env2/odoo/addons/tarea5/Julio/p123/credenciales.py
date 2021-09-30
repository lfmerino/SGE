def testUsuario(u):
    lmin = 6
    lmax = 12
        
    if len(u)<6: # Usuario al menos de 6 caracteres de longitud
        print("El nombre se usuario debe contener al menos 6 caracteres")
        Salida = 1
    elif len(u)>12: # Usuario de no más de 12 caracteres de longitud
        print("El nombre de usuario no puede tener más de 12 caractéres")
        Salida = 2
    elif not(u.isalnum()): # Usuario debe ser una cadena alfanumérica
        print("El nombre de usuario sólo puede contener caracteres alfanuméricos")
        Salida = 3
    else: # Nombre se usuario correcto
        print("Nombre de usuario válido")
        nombreUsuario = u
        return 0

def testPasswd(p):
        numCar = may = min = dig = noAlfNum = False
        esp = True
        lmin = 7

        if len(p) > lmin:
            numCar = True
        for c in p:
            if (not c.isspace()): # Comprobamos si hay espacios
                esp = False
            if c.isupper(): # Comprobamos si hay mayúsculas
                may = True
            if c.islower(): # Comprobamos si hay minúsculas
                min = True
            if c.isdigit(): # Comprobamos si hay números
                dig = True
            if not c.isalnum():
                noAlfNum = True # Comprobamos si hay espacios en blanco
        
        if (numCar and not esp and may and min and dig and noAlfNum):
            return 0
        else:
            return 1
