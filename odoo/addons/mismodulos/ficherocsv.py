#!/user/bin/env python 
# -*- coding: utf-8 -*-

import csv

class FicheroCSV:
	fichero=""

	#--- CONSTRUCTOR
	def __init__(self,fichero):
	 	self.fichero = fichero
	
	#--- METODOS
	def convertirDiccionario(self):
		dic={}
		reader = csv.reader(open(self.fichero, 'rb'))
		for i, row in enumerate(reader):
			dic[i+1]= row #creao un diccionario donde guardo un cada fila una lista 
							#(clave numero de la fila)
		return dic


	def Leer(self):
		reader = csv.reader(open(self.fichero, 'rb'))
		contenido='' #guardar contenido del fichero
		for i, row in enumerate(reader):
			linea ='' #guardar contenido de cada linea
			for j in range(0,len(row)): #desde cero hasta el numero de columnas
				if j != 0:
					linea = linea +','+row[j] #añadir columna a la lista
				else: linea = row[j]
			contenido = contenido+ linea + '\n'
			

		return contenido

	def numeroFilas(self):
		filas = len(open(self.fichero).readlines())
		return filas
	
	def numeroColumnas(self):
		reader = csv.reader(open(self.fichero, 'rb'))
		columnas = len( next(reader)) #next lee siguiente fila
		return columnas	

	def Escribir(self,dic):
		with open(self.fichero, 'wb') as f:
			writer = csv.writer(f,delimiter=',')
			writer.writerows(dic)
			
		
pass


