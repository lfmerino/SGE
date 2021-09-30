import psycopg2
from config import config
from tabulate import tabulate
import csv

class SqlPostgre():

    parametros=""

    def __init__(self):
        pass
    
    def conectar(self):
        try:
            parametros = config()
            print("Conectando a PostgreSQL...\n")
            self.conexion = psycopg2.connect(**parametros)
        except:
            print("OOps... Hubo un error conectando a PostgreSQL")
    
    def desconectar(self):
        try:
            if self.conexion:
                self.conexion.close()
        except:
            print("OOps... Hubo un error desconectando de PostgreSQL")

    def productos(self):
        self.conectar()
        try:
            # sql="SELECT ID, DEFAULT_CODE, NAME, DESCRIPTION FROM PRODUCT_TEMPLATE ORDER BY DESCRIPTION"
            sql='''select product_id as "ID Producto", f2.default_code as "Código Producto", name as "Descripción", sum(product_qty) as "Stock"
                    from stock_inventory_line f1, product_product as f2, product_template as f3
                    where product_id=f2.id and f2.product_tmpl_id=f3.id
                    group by "ID Producto", "Código Producto", "Descripción"
                    order by "Descripción"'''
            cur = self.conexion.cursor()
            cur.execute(sql)
            consulta = cur.fetchall()
            resultado=[["ID Producto", "Código", "Descripción", "Stock"]]
            for product_id, default_code, name, stock in consulta:
                # print ("{}\t{}\t{}\t{}".format(ID, DEFAULT_CODE, NAME, DESCRIPTION))
                resultado.append([product_id, default_code, name, stock])
            print(tabulate(resultado, headers='firstrow', tablefmt='psql', stralign='left' ))
            self.desconectar()
        
        except:
            self.desconectar()
            print("OOps... Hubo un problema al ejecutar la consulta de productos")

    def producto(self):
        self.conectar()
        id = input("Introduzca el 'id' del producto: ")
        try:
            # sql="SELECT ID, DEFAULT_CODE, NAME, DESCRIPTION FROM PRODUCT_TEMPLATE where ID = {} ORDER BY DESCRIPTION".format(id)
            sql='''select product_id as "ID Producto", f2.default_code as "Código Producto", name as "Descripción", sum(product_qty) as "Stock"
                    from stock_inventory_line f1, product_product as f2, product_template as f3
                    where product_id=f2.id and f2.product_tmpl_id=f3.id and product_id = {}
                    group by "ID Producto", "Código Producto", "Descripción"
                    order by "Descripción"'''.format(id)
            cur = self.conexion.cursor()
            cur.execute(sql)
            consulta = cur.fetchall()
            resultado=[["ID Producto", "Código", "Descripción", "Stock"]]
            for product_id, default_code, name, stock in consulta:
                # print ("{}\t{}\t{}\t{}".format(ID, DEFAULT_CODE, NAME, DESCRIPTION))
                resultado.append([product_id, default_code, name, stock])
            print(tabulate(resultado, headers='firstrow', tablefmt='psql', stralign='left' ))
            self.desconectar()
            pass

        except:
            print("OOps... Hubo un problema al buscar el producto")

    def salvarCSV(self):
        self.conectar()
        try:
            # sql="SELECT ID, DEFAULT_CODE, NAME, DESCRIPTION FROM PRODUCT_TEMPLATE ORDER BY DESCRIPTION"
            sql='''select product_id as "ID Producto", f2.default_code as "Código Producto", name as "Descripción", sum(product_qty) as "Stock"
                    from stock_inventory_line f1, product_product as f2, product_template as f3
                    where product_id=f2.id and f2.product_tmpl_id=f3.id
                    group by "ID Producto", "Código Producto", "Descripción"
                    order by "Descripción"'''
            cur = self.conexion.cursor()
            # print(sql)
            cur.execute(sql)
            consulta = cur.fetchall()
            datos=[["ID Producto", "Código", "Descripción", "Stock"]]
            for product_id, default_code, name, stock in consulta:
                datos.append([product_id, default_code, name, stock])
            
            ficheroCSV = open('SGEStock.csv', 'w', newline="")
            with ficheroCSV:
                writer = csv.writer(ficheroCSV)
                writer.writerows(datos)
        
                print("Escritura finalizada")
            self.desconectar
        except:
            print("OOps... Hubo un error salvando el archivo")