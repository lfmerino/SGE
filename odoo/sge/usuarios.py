# -*- coding: utf-8 -*-

def username(usuario):
	
	long=len(usuario) #Calcula la longitud de la cadena de caracteres
	x=usuario.isalnum() #Calcula que la cadena de caracteres sea alfanumérico
	y=long >5 and long <13 and x ==True #La variable y es igual al nombre de usuario correcto
	
	if long <6: #Comprueba si tiene menos de 6 caracteres
		print ("El nombre de usuario debe contener al menos 6 caracteres")
	
	elif long >12: #Comprueba si tiene más de 12 caracteres
		print ("El nombre de usuario no puede contener más de 12 caracteres")
	
	elif x== False: #Comprueba que no es alfanumérico
		print ("El nombre de usuario puede contener solo letras y números")
	
	elif long >5 and long <13 and x ==True: #Comprueba que tenga entre 6 y 12 caracteres y que sea alfanumérico
                print ("El nombre de usuario es válido")
	
	if y== True: #Si la variable y es true devuelve true y el usuario estaria creado
		return True
