import psycopg2
from config import config
from tabulate import tabulate
 
def conectar():
    
    conexion = None
    try:
        # Lectura de los parámetros de conexion
        params = config()
 
        # Conectamos servidor de PostgreSQL
        print('Conectando a PostgreSQL...')
        conexion = psycopg2.connect(**params)
 
        # Cursor para la base de datos
        cur = conexion.cursor()
        
        # Version de PostgreSQL
        print('La version de PostgreSQL es la:')
        cur.execute('SELECT version()')
         # Version
        version = cur.fetchone()
        print(version)
        print("\n +++++++++++++++++++++++++ \n")
        
        # cur.execute('SELECT ID, DEFAULT_CODE, NAME, DESCRIPTION FROM PRODUCT_TEMPLATE ORDER BY DESCRIPTION')
        cur.execute('SELECT ID, DEFAULT_CODE, NAME, DESCRIPTION FROM product.template.search.stock.form ORDER BY DESCRIPTION')
        consulta = cur.fetchall()
        resultado=[["ID", "REFERENCIA", "NOMBRE", "DESCRIPCION"]]
        for ID, DEFAULT_CODE, NAME, DESCRIPTION in consulta:
            # print ("{}\t{}\t{}\t{}".format(ID, DEFAULT_CODE, NAME, DESCRIPTION))
            resultado.append([ID, DEFAULT_CODE, NAME, DESCRIPTION])
        print(tabulate(resultado, headers='firstrow', tablefmt='psql', stralign='left' ))
       
        # Cerramos la conexión con PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conexion is not None:
            conexion.close()
            print('Conexión finalizada.')
 
 
if __name__ == '__main__':
    conectar()