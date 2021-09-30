class Passwd:

    def test_Passwd(self,passwd):
        numCar = may = min = dig = noAlfNum = False
        esp = False
        lmin = 7

        if len(passwd) > lmin:
            numCar = True
        for c in passwd:
            if c.isspace(): # Comprobamos si hay espacios
                esp = True
            if c.isupper(): # Comprobamos si hay mayúsculas
                may = True
            if c.islower(): # Comprobamos si hay minúsculas
                min = True
            if c.isdigit(): # Comprobamos si hay números
                dig = True
            if not c.isalnum():
                noAlfNum = True
        
        if (numCar and not esp and may and min and dig and noAlfNum):
            return 0
        else:
            return 1
