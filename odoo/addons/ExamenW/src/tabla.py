# -*- coding: utf-8 -*-

from datetime import date
from datetime import datetime
import csv
import random
import modulo1
#import bdpostgres
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
        self.cApellidos = pCliente['nombre'][pCliente['nombre'].find(" ")+1:].strip()
        self.cEmail= pCliente['email']
        self.cCP= pCliente['sexo']
        self.cLogin=self.cNIF[:1].lower()+self.cApellidos[:self.cApellidos.find(" ")].lower()
        self.hacercontrasena()
        if self.cCP=="H":
            self.cSignature="Sr. "+self.cApellidos
        else:
            self.cSignature="Sra. "+self.cApellidos
        
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

    def hacercontrasena(self):
        elegir=[self.cNombre,self.cApellidos[:self.cApellidos.find(" ")],self.cApellidos[self.cApellidos.find(" ")+1:]]
        #print(elegir)
        sel=random.choice((0,1,2))
        elem0=elegir[sel]
        elegir.pop(sel)
        sel=random.choice((0,1))
        elem1=elegir[sel]
        elegir.pop(sel)
        elem2=elegir[0]
        #print(elem0,elem1,elem2)
        horaactual = datetime.now()
        #self.cContrasena=elem0[:1]+str(horaactual.second)+elem1[1:2]+elem1[2:3].upper()+str(horaactual.minute)+elem2[3:4]+random.choice(("$","%","&"))
        self.cContrasena=modulo1.Clave(elem0[:1]+str(horaactual.second)+elem1[1:2]+elem1[2:3].upper()+str(horaactual.minute)+elem2[3:4]+random.choice(("$","%","&"))).MiNombre
       # print(self.cContrasena)           
        



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
           
        
        with open('/home/luis/Desktop/Instituto/Dropbox/Mi PC (LAPTOP-NS9I1DS1)/Desktop/SGE/odoo/addons/examen/usuarios.csv', encoding="utf8") as File:  
        #print("Recuperar")
        #with open('C:/Users/dptoinformatica/Dropbox/Mi PC (LAPTOP-NS9I1DS1)/Desktop/SGE/odoo/addons/examen/usuarios.csv', encoding="utf8") as File:
            reader = csv.DictReader(File)  
            vCont=0
            for row in reader:
                vCliente=Cliente(False,row)
                self.dTabla[vCliente.cNIF]=vCliente
                vCont += 1
            print("Leídos "+str(vCont)+" registros")
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
   
    def InsertarUsuarios(self,bd):
        #tCampos=['NIF','APELLIDOS','NOMBRE','FECHA NACIMIENTO','TELÉFONO MÓVIL','CORREO ELECTRÓNICO']
#        tCampos=['NIF','APELLIDOS','NOMBRE','EMAIL','SEXO']
        vContContactos=0 # Contar altas en contactos
        vContUsuarios=0 #cContar altas de usuarios
        vContActUsuarios=0 # Contar actualizaciones de usuarios
        vClaves=self.dTabla.keys()
        for mClave in vClaves:
            #print("SELECT id FROM res_partner WHERE name='"+self.dTabla[mClave].cNombre+ " " + self.dTabla[mClave].cApellidos + "'")
            #si no existe la persona en res_partner, se crea
            if (not bd.ConsultaDic("SELECT id FROM res_partner WHERE name='"+self.dTabla[mClave].cNombre+ " " + self.dTabla[mClave].cApellidos + "'")):
                #Si no existe la persona la añade a res_partner
                fecha=str(datetime.now())
                bd.ConsultaDic("insert into res_partner (name, create_date, display_name, lang, email, commercial_partner_id, create_uid, write_uid, write_date) VALUES ('"
                +self.dTabla[mClave].cNombre+ " " + self.dTabla[mClave].cApellidos + "','"+fecha+"','"
                +self.dTabla[mClave].cNombre+ " " + self.dTabla[mClave].cApellidos+"','es_ES','"+self.dTabla[mClave].cEmail+"',1,1,1,'"
                +fecha+"');")
                vContContactos += 1 
               
                #print("insert into res_partner (name, create_date, display_name, lang, email, commercial_partner_id, create_uid, write_uid, write_date) VALUES ('"
                #+self.dTabla[mClave].cNombre+ " " + self.dTabla[mClave].cApellidos + "','"+fecha+"','"
                #+self.dTabla[mClave].cNombre+ " " + self.dTabla[mClave].cApellidos+"','es_ES','"+self.dTabla[mClave].cEmail+"',1,1,1,'"
                #+fecha+"');")
            
            #obtener id de la persona
            filas = bd.ConsultaDic("SELECT id FROM res_partner WHERE name='"+self.dTabla[mClave].cNombre+ " " + self.dTabla[mClave].cApellidos + "'")
            #Si el usuario existe en res_users, entonces actualizar, si no crear
           
           # for fila in filas: #recorre todos las filas q te devuelve el select
           
            #if filas:
                #print(filas)
            vpersona=str(filas[0][0]) # solo coge el primer resultado
            #else:
                #print("Vacía")
                #vpersona=str(100)
            #    break
            #print(vpersona)
            fecha=str(datetime.now())
            if (bd.ConsultaDic("SELECT id FROM res_users WHERE login='"+self.dTabla[mClave].cLogin + "'")):
                #Si existe el usuario, lo actualiza
                bd.ConsultaDic("UPDATE res_users SET password='" +self.dTabla[mClave].cContrasena+"', signature='"+self.dTabla[mClave].cSignature + "', write_date='"+ fecha + "',write_uid=2 WHERE login='"+self.dTabla[mClave].cLogin+"';")
                vContActUsuarios += 1
                #print("UPDATE res_users SET password='" +self.dTabla[mClave].cContrasena+"' signature='"+self.dTabla[mClave].cSignature + "', write_uid='"+ fecha + "' WHERE login='"+self.dTabla[mClave].cLogin+"';")
            else:
                #Si no existe lo añde
                bd.ConsultaDic("INSERT INTO res_users (login, password, company_id, partner_id, create_date, signature, create_uid, write_uid, write_date, notification_type) VALUES ( '"+self.dTabla[mClave].cLogin+"', '"+self.dTabla[mClave].cContrasena+"', 1,"+ vpersona+",'"+fecha+"', '"+self.dTabla[mClave].cSignature+"', 2, 2, '"+fecha+"','email');")
                vContUsuarios += 1
                #print("INSERT INTO res_users (login, password, company_id, partner_id, create_date, signature, create_uid, write_uid, write_date, notification_type) VALUES ( '"+self.dTabla[mClave].cLogin+"', '"+self.dTabla[mClave].cContrasena+"', 1,"+ vpersona+",'"+fecha+"', '"+self.dTabla[mClave].cSignature+"', 2, 2, '"+fecha+"','email');")
        print("Contactos creados: "+str(vContContactos)+"\nUsuarios creados: "+str(vContUsuarios)+"\nUsuarios actualizados: "+str(vContActUsuarios))
