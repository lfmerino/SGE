#!/user/bin/env python 
# -*- coding: utf-8 -*-

import psycopg2
import sys

class BD:
	#--- ATRIBUTOS
	conexion = None
	puntero = None
	
	
	#--- CONSTRUCTOR
	def __init__(self):
		self.conexion = None
		self.puntero = None
	

	#--- MEDOTOS
	def CrearConexion(self,bd,u,h,psw,p):
		try:
			self.conexion = psycopg2.connect(dbname=bd, user=u, host=h, password=psw, port=p)
			self.puntero = self.conexion.cursor()
			return True	
		except ValueError:
			return False	
		
	

	
		
	# metodos para realizar operaciones

	def Consulta(self,sentencia):
		#puntero = self.conexion.cursor()
		try:
			self.puntero.execute(sentencia)
			
		#except  psycopg2.ProgrammingError: #Error si la tabla no existe
			#return 'Error'
		except Exception :
			return 'Error'



		if sentencia.upper().startswith('SELECT'): 
			rows = self.puntero.fetchall()
			#rows = puntero.fetchall()
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

			return linea
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

	def ConsultaDic(self,sentencia):
		#puntero = self.conexion.cursor()
		try:
			self.puntero.execute(sentencia)
			#puntero.execute(sentencia)
		except Exception:
			return 'Error al ejecutar sentencia'
		except  psycopg2.ProgrammingError: #Error si la tabla no existe
			return 'Error al ejecutar sentencia'
		
		
		if sentencia.upper().startswith('SELECT'): 
			rows = self.puntero.fetchall()
			return rows

	def CerrarConexion(self):
		self.puntero.close()
		self.conexion.close()
pass
#self.conexion = psycopg2.connect(dbname=self.bd, user=self.u, host=self.h, password=self.psw, port=self.p)

