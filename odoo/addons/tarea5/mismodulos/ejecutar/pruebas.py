cadena=input("Comprobar: ")
if (any(letra.islower() for letra in cadena)):
    print("En la cadena hay minúsculas")