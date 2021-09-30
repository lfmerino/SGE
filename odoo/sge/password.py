# -*- coding: utf-8 -*-

def clave(password):
	
	long=len(password) #Calcula la longitud de la cadena de caracteres
	x=password.isalnum() #Calcula que la cadena de caracteres es alfanúmerica
	num=False #Guarda si tiene números
	may=False #Guarda si tiene mayúsculas
	min=False #Guarda si tiene minúsculas
	
	if long < 8 and x== True: #Comprueba que tiene más de 8 caracteres y no es alfanúmerico
		return False
	
	for car in password: #Comprueba que son verdaderas todas las condiciones
	
		if car.isspace(): #Comprueba si tiene espacios
			return False
	
		if car.isdigit(): #Comprueba si tiene números
			num=True
	
		if car.isupper(): #Comprueba si tiene mayúsculas
			may=True
	
		if car.islower(): #Comprueba si tiene minúsculas
			min=True
	
	if num==True and may==True and min==True: #Devuelve true si contiene al menos caracter num, may, min
		return True
