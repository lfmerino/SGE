#!/user/bin/env python 
# -*- coding: utf-8 -*-

#from odoo.addons.mismodulos import tabla
#from odoo.addons.mismodulos import bdpostgres

import tabla
import bdpostgres

#import csv
import sys

#import time
# --------------------------------------------
#       METODOS PRINCIPAL
# --------------------------------------------


def InsertarUsuarios():
    
    MiTabla.InsertarUsuarios(db)

def Salir():
  #  try:
        #print
    #sys.exit()
    #quit()
    exit()
    #except:
     #   print("Error inesperado:", sys.exc_info()[0])
    




def error():
        #os.system ("cls") 
        print('La opción seleccionada no es válida')

def Menu():
    #os.system ("cls") 
   
    print ("1 - Recuperar datos de un CSV")
    print ("2 - Insertar datos de usuarios")
    #print ("3 - Salvar datos en CSV")
    print ("5 - Salir")
    print (" ------------------------------ ") 
    #return input (("Elige una opcion: "))
    try:
        return int(input ("Elige una opción: "))
    except:
        return 100
# --------------------------------------------
#                 PRINCIPAL
# --------------------------------------------
dbname='Zaxeboa'
user='odoo'
host='192.168.56.101'
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
if (input("¿Cambiar parámetros?(S/N)").upper()=="S"):
    dbname = input('\tIntroduce nombre de la base de datos> ')
    user = input('\tIntroduce usuario> ')
    host = input('\tIntroduce host> ')
    password = input('\tIntroduce contraseña> ')
    port = input('\tIntroduce puerto> ')

db = bdpostgres.BD()

if db:
    db.CrearConexion(dbname,user,host,password,port)

    MiTabla=tabla.DicClientes()


    switch_menu = {
            0: Menu,
            1: MiTabla.Recuperar,
            2: InsertarUsuarios,
            #3: MiTabla.Guardar,
            #4: MiTabla.Recuperar,
            #4: cargar,
            5: Salir,
    }

    opc=Menu()
    #while opc!=5:
     #   switch_menu.get(opc, error)()
    while opc>0:
        
        switch_menu.get(opc, error)()
        opc=Menu()

    db.CerrarConexion()




