class Usuario:

    def test_Nombre(self,l):
        lmin = 6
        lmax = 12
        
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
