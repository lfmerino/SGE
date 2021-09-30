#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 23:17:38 2021

@author: luis
"""



'''print '\n======================================================'
print '\tUSUARIOS'
print '======================================================'

print '-------------------------------------------------'
print '\t CONECTAR CON LA BASE DE DATOS '
print '-------------------------------------------------'
'''
'''dbname = raw_input('\tIntroduce nombre de la base de datos> ')
user = raw_input('\tIntroduce usuario> ')
host = raw_input('\tIntroduce host> ')
password = raw_input('\tIntroduce contraseña> ')
port = raw_input('\tIntroduce puerto> ')
'''

'''dbname='Libreria'
user='postgres'
host='10.22.100.44'
#host ='192.168.1.76'
password='virgi'
port='5432'

db = modulos.BDpostgres.BD()

datos = db.CrearConexion(dbname,user,host,password,port)


while datos==False:
	print 'Datos no validos. Introducir datos correctos:'

	dbname = raw_input('\tIntroduce nombre de la base de datos> ')
	user = raw_input('\tIntroduce usuario> ')
	host = raw_input('\tIntroduce host> ')
	password = raw_input('\tIntroduce contraseña> ')
	port = raw_input('\tIntroduce puerto> ')


	datos = db.CrearConexion(dbname,user,host,password,port)
print 'Conectado a la base de datos...'

#Vble q voy a usar despues
result=''
op='s'#para entrar en el while

while True:	
	
	if op=='S' or op=='s':
		print '-------------------------------------------------'
		print '\t FICHERO CON DATOS '
		print '-------------------------------------------------'
		
		nom = raw_input('\tIntroduce nombre del fichero> ')
		nom ='usuarios.csv'
		
		directorioActual = '{0}'.format(os.getcwd()) + '/'+ nom
		#print directorioActual
		
		if os.path.isfile(directorioActual): #metodo comprueba si el fichero existe
			fic =  modulos.FicheroCSV.FicheroCSV(nom)
			

			res = raw_input('\t¿Desea visualizar el fichero? s/n> ')
			if res=='s' or res=='S':
				print '-------------------------------------------------'
				print '\t VISUALIZR FICHERO '+ nom
				print '-------------------------------------------------'
				print fic.Leer()	
				print '-------------------------------------------------'
		

		
			res = raw_input('\t¿Desea insertar o modificar los usuarios? s/n> ')
			if res=='s' or res=='S':
				#obtener diccionario con contenido del fichero
				dic = fic.convertirDiccionario()
				for i in dic:
					fila = dic[i]
					comprobarUsuario(fila[0],fila[1],fila[2])

		else:
			print 'El fichero no existe'
		print '-------------------------------------------------'
	

	else:
		print 'FIN PROGRAMA\n'
		
		break

	op = raw_input ("¿DESEA CONTINUAR? S/N: ")
	print '======================================================\n'


print '-------------------------------------------------'
print '\t COSULTAR USUARIO '
print '-------------------------------------------------'

op='s'#para entrar en el while

while True:	
	
	if op=='S' or op=='s':
		print '-------------------------------------------------'
		print '\t LISTADO DE USUARIOS '
		print '-------------------------------------------------'
		print  db.Consulta("SELECT name FROM res_users" )
		
		nom = raw_input ("\nIntroducir nombre de usuario> ")
		res = db.ConsultaDic("SELECT name,signature,login,password FROM res_users WHERE name='"+ nom+"'" )
		if res =='':
			print 'No existe'
		else:
			print res
			f = raw_input('\tIntroduce nombre del fichero> ')
			ficUsu =  modulos.FicheroCSV.FicheroCSV(f)
			ficUsu.Escribir(res) #añade al fichero no sobreescribe
	
			res = raw_input('\t¿Desea visualizar el fichero? s/n> ')
			if res=='s' or res=='S':
				print '\n==================================================='
				print '\t VISUALIZR FICHERO '+ nom
				print '==================================================='
				print ficUsu.Leer()
			print '===================================================\n'
	

	else:
		print 'FIN PROGRAMA\n'
		
		break
	op = raw_input ("¿DESEA CONTINUAR? S/N: ")
	print '======================================================\n'

db.CerrarConexion()

	def Consulta(self,sentencia):
		#puntero = self.conexion.cursor()
		try:
			self.puntero.execute(sentencia)
			
		#except  psycopg2.ProgrammingError: #Error si la tabla no existe
			#return 'Error'
		except Exception :
			return 'Error'



		if sentencia.upper().startswith('SELECT'):
            return self.puntero.fetchall()
	'''		#rows = puntero.fetchall()
			linea=''
			aux=0
			for row in rows: #recorre todos las filas q te devuelve el select
				aux = aux+1
				#print len(rows[0])
				for i in range(0,len(rows[0])): # recorre las columnas y lo concatena en un string
					if i < len(rows[0])-1:
						linea = linea + str(row[i]) + ','
					else:
						linea = linea + str(row[i]) #para q al final no aparezca una coma
				#print len(rows)
				if aux < len(rows):
					linea = linea+'\n'

			return linea'''
		else:
			self.conexion.commit()
			if sentencia.upper().startswith('INSERT'): 
				return 'Insertado'
			elif sentencia.upper().startswith('UPDATE'): 
				return 'Modificado'
			elif sentencia.upper().startswith('DELETE'): 
				return 'Eliminado'
			else:
				return 'commit'
                
                
                
                	# metodos para realizar operaciones


def ConsultaDic(self,sentencia):
    #puntero = self.conexion.cursor()
    try:
        if sentencia.upper().startswith('SELECT'):
            return self.puntero.fetchall()
        else:
            self.puntero.execute(sentencia)
            #puntero.execute(sentencia)
    except Exception:
        return 'Error al ejecutar sentencia'
def CerrarConexion(self):
    self.puntero.close()
    self.conexion.close()

