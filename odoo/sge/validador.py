# -*- coding: utf-8 -*-

import usuarios
import password

validar=False #Asignamos false a la variable

while validar==False: #Si validar es false comprueba lo siguiente
	nombre=input("Nombre usuario:") #Pide el nombre por pantalla
	if usuarios.username(nombre)== True: #Comprueba que el nombre es verdadero
		print ("Usuario creado")
		validar=True #Cambia la variable a true

while validar==True: #Si validar es true cmprueba lo siguiente
        passwd=input("Password:") #Pide la contraseña por pantalla
        if password.clave(passwd)== True: #Cmprueba que la contraseña es verdadera
                print ("Password creado")
                validar=False #Cambia la variable a false

