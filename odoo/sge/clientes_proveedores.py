# -*- coding: utf-8 -*-

import psycopg2
import pandas as pd
import csv

conexion = psycopg2.connect (host="localhost",
                                database="Odoo14",
                                user="postgres",
                                password="Carla2017")

cursor = conexion.cursor()

with open ('clientes.csv','r') as f:
#	reader = csv.reader(f)
#	next(reader)
#	for row in reader:
#		cursor.execute ("INSERT INTO res_partner VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
#		row
#	)
#conexion.commi()
	cursor.copy_from(f, 'res_partner',sep= ';')

conexion.commi()


#df = pd.read_sql_query("SELECT * FROM res_partner order by id ",conexion)
#print ("\n", df)

#tabla = "SELECT * FROM PUBLIC.res_partner where type = 'contact' order by id "

#cursor.execute(tabla)

#filas = cursor.fetchall()
#for fila in filas:
#	print (fila)
#	with open ('clientes.csv','w',newline='')as archivo:
#		writer = csv.writer(archivo,delimiter=';')
#		writer.writerows(filas)
#conexion.commit()


#with open ('clientes.csv','r') as tabla:

 #       cursor.copy_from(tabla, 'res_partner',sep= ';')

conexion.commit()
conexion.close()
