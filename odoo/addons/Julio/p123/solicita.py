import credenciales as func

for cont in range(3):
    u = input("Introduzca el nombre de usuario: ")
    if (func.testUsuario(u) == 0):
        # Aqui haremos lo que queramos. Ahora tengo mensajes en el método pero los quitaría
        print('Ya hemos cambiado el usuario')
    else:
        # Otras cosas que queramos hacer
        print("No hemos podido cambiar el usuario\n")
        print("Quedan {} intentos".format(2-cont))

for cont in range(3):
    contraseña = input("Introduzca la contraseña: ")
    if (func.testPasswd(contraseña)== 0):
        # Lo mismo que con el usuario pero con la contraseña
        print("Hemos cambiado la contraseña")
    else:
        # Idem
        print("No hemos cambiado la contraseña")
        print("Quedan {} intentos".format(2-cont))
