#!/user/bin/env python 
# -*- coding: utf-8 -*-

from odoo.addons.mismodulos import tabla
from odoo.addons.mismodulos import bdpostgres
import csv
import sys
import os
import time
# --------------------------------------------
#       METODOS PRINCIPAL
# --------------------------------------------
def sacarApellidos(nom):
	try:
		pos = nom.index(' ') #posicion donde se los blancos
		ape = nom[pos+1:len(nom)]#quita el nombre	
		pos = ape.index(' ')
		ape1 = ape[0:pos]#primer apellido
		pos = ape.index(' ')
		ape2 = ape[pos+1:len(ape)]
		print(ape2)
	except ValueError:
		ape1 = ape #si no tiene segundo apellido hasta el final
		ape2 = ''
	return [ape1,ape2]
	
def crearLogin(nom):
	try:
		login = nom[0]
		pos = nom.index(' ') #posicion donde se los blancos
		ape = nom[pos+1:len(nom)]
		pos = ape.index(' ')
		ape = ape[0:pos]
		login = login+ape

	except ValueError:
		login = login+ape #si no tiene segundo apellido hasta el final
	return login.lower()
	
def crearAsignature(nom,sexo):
	try:
		if sexo=='H':
			asignature ='Sr. '
		else:
			asignature ='Sra. '
		#obtener apellido
		pos = nom.index(' ') #posicion donde se los blancos
		ape = nom[pos+1:len(nom)]
		pos = ape.index(' ')
		ape = ape[0:pos]
		asignature = asignature+ape
	except ValueError:
		asignature = asignature+ape
        #si no tiene segundo apellido hasta el final
	
	return asignature
	


def comprobarUsuario(nom,email,sexo):

	#COMPROBAR SI EXISTE EL USUARIO
	'''nom_usu = db.Consulta("SELECT name FROM res_users WHERE name='"+ nom+"'" )
	#print nom_usu
	if nom_usu != nom:
		InsertarUsuario(nom,email,sexo)
	else:
		ModificarUsuario(nom,email,sexo)'''

def crearPassword(nom):
	ps = nom[0]
	try:
		ape = sacarApellidos(nom) #posicion donde se los blancos
		ape1 = ape[0]
		ape2 = ape[1]
		ps = ps = ps +  time.strftime("%S") +ape1[1] +ape1[2].capitalize() +time.strftime("%M") + ape2[3] + '%'
	except IndexError:
		ps = ps = ps +  time.strftime("%S") +time.strftime("%M")  + '%'
    	

	return ps

def validarContrasena(constrasena):
	if (constrasena.isalnum() == True or len(constrasena) < 8 or constrasena.isspace() == True):
		return False
	else:
		return True



def InsertarUsuario(nom,email,sexo):
	login = crearLogin(nom)
	asignature = crearAsignature(nom,sexo)
	password = crearPassword(nom)
	#print password
	
	
	sql = "INSERT INTO res_users (name, active, login, password, email, company_id ,create_uid, create_date, write_date, write_uid, menu_id, menu_tips,signature) VALUES ('"+nom+"', True, '"+login+"', '" +password+ "', '" +email+ "',1,1, current_date , current_date, 1, 1,FALSE,'"+ asignature+"')"
	print("sql> " + sql)
	
	#print( "\t" + db.Consulta(sql) +' ' + nom)
	
	
def ModificarUsuario(nom,email,sexo):
	
	#obtener id para modificar el cliente si existe 
	'''sql = "SELECT id FROM res_users WHERE name='"+ nom + "'"
	id = db.Consulta(sql)
	if id!='':	
		login = crearLogin(nom)
		signature = crearAsignature(nom,sexo)
		password = crearPassword(nom)	
		sql = "UPDATE res_users SET email='"+email+"',login='"+login+"', password='"+ password+"', signature='"+signature+"' WHERE id=" +id
		#print "sql> " + sql
		
		print(db.Consulta(sql)  +' ' + nom)'''
	


def cargar():
    MiTabla.Recuperar()
    MiTabla.InsertarUsuarios()
    



def Salir():
	sys.exit()

def error():
	print('La opción seleccionada no es válida')

def Menu():
   # os.system ("cls") 
    print("Pepe")
    print ("1 - Introducir datos del usuario")
    print ("2 - Buscar usuario")
    print ("3 - Salvar datos en CbbbV")
    print ("4 - Recuperar datos de un CSV")
    print ("0 - Salir")
    print (" ------------------------------ ") 
    return int(input ("Elige una opcion: "))

# --------------------------------------------
#                 PRINCIPAL
# --------------------------------------------
dbname='Zaxeboa'
user='odoo'
fhost='192.168.56.101'
password='Brianda20'
port='5432'

print("Parámetros para conectar a la base de datos")
print("Servidor: "+host+"\nPuerto: "+port+"\nUsuario: "+user+"\nContraseña: "+password+"\nBase de Datos: "+dbname)

'''
print '\n======================================================'
print '\tUSUARIOS'
print '======================================================'

print '-------------------------------------------------'
print '\t CONECTAR CON LA BASE DE DATOS '
print '-------------------------------------------------'
'''
if (input("¿Desea cambiar parámetros?(S/N)").upper()=="S"):
    dbname = input('\tIntroduce nombre de la base de datos> ')
    user = input('\tIntroduce usuario> ')
    host = input('\tIntroduce host> ')
    password = input('\tIntroduce contraseña> ')
    port = input('\tIntroduce puerto> ')

db = bdpostgres.BD()


datos = db.CrearConexion(dbname,user,host,password,port)
 
MiTabla=tabla.DicClientes()


switch_menu = {
	0: Menu,
    1: MiTabla.Datos,
	2: MiTabla.Buscar,
	3: MiTabla.Guardar,
	#4: MiTabla.Recuperar,
    4: cargar,
	5: Salir,
}

opc=Menu()
while opc>0:
    switch_menu.get(opc, error)()
    opc=Menu()

db.CerrarConexion()




