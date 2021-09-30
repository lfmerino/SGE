# -*- coding: utf-8 -*-

import psycopg2
import pandas as pd
import csv

conexion = psycopg2.connect (host="localhost",
				database="Odoo14",
				user="postgres",
				password="Carla2017")

cursor = conexion.cursor()


df = pd.read_sql_query('''SELECT product_product.id, product_product.default_code,
product_template.name FROM product_product, product_template
where product_product.product_tmpl_id = product_template.id
order by id ''',conexion)
print ("\n", df)

input ("\n Esta es la tabla de los productos, presiona enter para ver articulos con stock")

print ("\n")

registros = '''select product_product.id, product_product.default_code,
product_template.name, stock_quant.quantity
from product_product, stock_quant, product_template
where stock_quant.product_id = product_product.id and location_id = 8
and product_product.product_tmpl_id = product_template.id
order by product_product.id '''

#registros = "select stock_quant.quantity from stock_quant"
#where stock_quant.product_id = 17
#and purchase_order_line.product_id = 17 and location_id = 8

#nombre = input("Seleciona id: ")

cursor.execute(registros)
filas = cursor.fetchall()
for fila in filas:
#	if (nombre in fila):
	print ("Id:", fila[0],"Codigo:", fila[1], "Descripcion:", fila[2], "Cantidad stock:", fila[3])
#	print ("\n")
#	print (fila)

#nombre = input()
#if (nombre in fila):
#	print (fila)

input("\n Presiona enter para crear un archivo .csv con los productos en stock")

print ("\n")

tabla = '''select product_product.id, product_product.default_code,
product_template.name, stock_quant.quantity
from product_product, stock_quant, product_template
where stock_quant.product_id = product_product.id and location_id = 8
and product_product.product_tmpl_id = product_template.id
order by product_template.name '''

cursor.execute(tabla)

#tabla.to_csv('/usr/python3/dist-packages/odoo/addons/sge/tarea5.5.csv')

filas = cursor.fetchall()
for fila in filas:
	#print ("Id:", fila[0],"Codigo:", fila[1], "Descripcion:", fila[2], "Cantidad stock:", fila[3])

	with open ('tarea5.csv','w',newline='')as archivo:
		writer = csv.writer(archivo,delimiter=';')
		writer.writerows(filas)

print (" El archivo se ha creado correctamente\n")

conexion.commit()
conexion.close()
