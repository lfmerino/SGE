# -*- coding: utf-8 -*-

from datetime import date
import csv
import random
import time
'''from datetime import datetime
import sys
import os

'''
class Cliente:
    
    cApellidos="Apellido1 Apellido2"
    cNombre="Nombre"
    cNIF="0T"
    cFecNac=date.today()
    cDireccion="Calle"
    cUsuario="Usuario"
    cContrasena="C@mb1@r21"
    cCP="00000"
    cPoblacion="Guadalajara"
    cProvincia="Guadalajara"
    cTfno=999999999
    cEmail="p@s.es"
    cLogin="Usuario"
    cSignature="Sra."

    def __init__(self,opc=True,pCliente={}):
        if opc:
            self.pedirDatos()
        else:
            self.completarDatos(pCliente)
   
    def pedirDatos(self):
        self.cNIF = input("NIF: ")
        self.cApellidos = input("Apellidos: ")
        self.cNombre = input("Nombre: ")
        self.cEmail = input("Email: ")
        self.cCP = input("Sexo: ")
#   self.cFecNac = input("Fecha de nacimiento: ")
 #       self.cDireccion = input("Dirección: ")
  #      self.cCPn = input("CP: ")
   #     self.cPoblacion=input("Población: ")
    #    self.cProvincia=input("Provincia: ")
     #   self.cTfno=input("Teléfono: ")'''

                
    def completarDatos(self,pCliente):
    #def 
        #print(pCliente)
        
        self.cNIF = pCliente['nombre'][:pCliente['nombre'].find(" ")]
        self.cNombre = pCliente['nombre'][:pCliente['nombre'].find(" ")]
        self.cApellidos = pCliente['nombre'][pCliente['nombre'].find(" ")+1:]
        self.cEmail= pCliente['email']
        self.cCP= pCliente['sexo']
        self.cLogin = (self.cNombre[:1]+self.cApellidos[:self.cApellidos.find(" ")]).lower()
        if self.cCP=="M":
            self.cSignature="Sra."+self.cApellidos[:self.cApellidos.find(" ")]
        else:
           self.cSignature="Sr."+self.cApellidos[:self.cApellidos.find(" ")]
        self.clave()
        
        #self.cEmail= pCliente['CORREO ELECTRÓNICO']
        #self.cCPn = input("CP: ")
        '''self.cNombre = pCliente['NOMBRE']
        self.cFecNac =  pCliente['FECHA NACIMIENTO']
        self.cDireccion = input("Dirección: ")
        
        self.cCPn = input("CP: ")
        self.cPoblacion=input("Población: ")
        self.cProvincia=input("Provincia: ")
        self.cTfno= pCliente['TELÉFONO MÓVIL']
        
        self.cNIF= pCliente['\ufeffDNI']'''
    def clave(self):
        elegir=[self.cNombre,
                self.cApellidos[:self.cApellidos.find(" ")-1],
                self.cApellidos[self.cApellidos.find(" ")+1:]]
        try:
            sel1=random.choice((0, 1, 2))
            self.cContrasena=elegir[sel1][:1]+time.strftime("%S")
            if sel1==2:
                sel1=0
                sel2=1
            else:
                sel1=sel1+1
                if sel1==1:
                    sel2=2
                else:
                    sel2=0
            self.cContrasena=self.cContrasena+elegir[sel1][1:2]+elegir[sel1][2:3].upper()+time.strftime("%M")+elegir[sel2][3:4]+random.choice(("$", "%", "&"))
        except ValueError:
            self.cContrasena="Cam5iar$"

print()

   


class DicClientes:
    dTabla = {}
    
    def __init__(self):
        pass

    def Datos(self):
        
        vOpc="S"
    
        while vOpc.upper()=="S":
            vCliente=Cliente()
            self.dTabla[vCliente.cNIF]=vCliente
            for clave in self.dTabla:
                print(self.dTabla[clave].cApellidos + ", " + self.dTabla[clave].cNombre)
            vOpc=input("Seguir(S/n)?: ")
            if vOpc=="":
                vOpc="S"
        del vCliente
                
    def Recuperar(self):
           
        #with open('/Users/dptoinformatica/Downloads/MiFichero.csv', encoding="utf8") as File:  
        with open('/home/luis/Desktop/Instituto/Dropbox/Mi PC (LAPTOP-NS9I1DS1)/Desktop/SGE/odoo/addons/examen/usuarios.csv', encoding="utf8") as File:  
  #/home/luis/Desktop/Instituto/Dropbox/Mi PC (LAPTOP-NS9I1DS1)/Desktop/SGE/odoo/addons/examen/usuarios.csv
            reader = csv.DictReader(File)  
            for row in reader:
                vCliente=Cliente(False,row)
                self.dTabla[vCliente.cNIF]=vCliente
                #print(vCliente.cNIF)
                

    

    def Buscar(self):
        '''for clave in self.dTabla:
                print(self.dTabla[clave].cApellidos + ", " + self.dTabla[clave].cNombre)'''
        vNIF=input("NIF para buscar: ")
        try:
            print(self.dTabla[vNIF].cApellidos + ", " + self.dTabla[vNIF].cNombre)
        except KeyError:
            print("Nombre no encontrado")


    def Guardar(self):
        #tCampos=['NIF','APELLIDOS','NOMBRE','FECHA NACIMIENTO','TELÉFONO MÓVIL','CORREO ELECTRÓNICO']
        tCampos=['NIF','APELLIDOS','NOMBRE','EMAIL','SEXO']
        with open('MiFicheroPrograma.csv',
        #/home/luis/Desktop/Instituto/Dropbox/Mi PC (LAPTOP-NS9I1DS1)/Desktop/SGE/odoo/addons/tarea5/ejecutar/MiFicheroPrograma.csv
                  'w', newline='') as file:
            vClaves=self.dTabla.keys()
            writer = csv.DictWriter(file, fieldnames=tCampos)
            writer.writeheader()
            for mClave in vClaves:
               ''' (print(self.dTabla[mClave].cNIF + " " + self.dTabla[mClave].cApellidos + " " + 
                self.dTabla[mClave].cNombre + " " + self.dTabla[mClave].cFecNac + " " + 
                self.dTabla[mClave].cTfno + " " + self.dTabla[mClave].cEmail))'''
               writer.writerow({tCampos[0] : self.dTabla[mClave].cNIF, \
                tCampos[1] : self.dTabla[mClave].cApellidos,tCampos[2] : self.dTabla[mClave].cNombre, \
                #tCampos[3] : self.dTabla[mClave].cFecNac,tCampos[4] : self.dTabla[mClave].cTfno, \
                tCampos[3] : self.dTabla[mClave].cEmail,tCampos[4] : self.dTabla[mClave].cCP})
   
    def InsertarUsuarios(self):
        #tCampos=['NIF','APELLIDOS','NOMBRE','FECHA NACIMIENTO','TELÉFONO MÓVIL','CORREO ELECTRÓNICO']
#        tCampos=['NIF','APELLIDOS','NOMBRE','EMAIL','SEXO']
        vClaves=self.dTabla.keys()
        for mClave in vClaves:
           print(self.dTabla[mClave].cNIF + " " + self.dTabla[mClave].cApellidos + " " + 
            self.dTabla[mClave].cNombre + " " + self.dTabla[mClave].cCP + " " + self.dTabla[mClave].cEmail
             + " " + self.dTabla[mClave].cLogin+ " " + self.dTabla[mClave].cContrasena
             + " " + self.dTabla[mClave].cSignature)
    
    
    '''

            
        
            
   


def Salir():
	sys.exit()

def error():
	print('La opción seleccionada no es válida')

def Menu():
   # os.system ("cls") 
    print ("1 - Introducir datos del usuario")
    print ("2 - Buscar usuario")
    print ("3 - Salvar datos en CSV")
    print ("4 - Recuperar datos de un CSV")
    print ("0 - Salir")
    print (" ------------------------------ ") 
    return int(input ("Elige una opcion: "))



 

MiTabla=DicClientes()

switch_menu = {
	0: Menu,
    1: MiTabla.Datos,
	2: MiTabla.Buscar,
	3: MiTabla.Guardar,
	4: MiTabla.Recuperar,
	5: Salir,
}

opc=Menu()
while opc>0:
    switch_menu.get(opc, error)()
    opc=Menu()
'''
