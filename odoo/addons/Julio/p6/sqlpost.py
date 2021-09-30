import psycopg2
from config import config
from tabulate import tabulate
from csv import DictReader
from clase_usuario import Usuario

class SqlPostgre():

    parametros=""

    def __init__(self):
        pass
    
    def conectar(self):
        try:
            parametros = config()
            # print("Conectando a PostgreSQL...\n")
            self.conexion = psycopg2.connect(**parametros)
        except:
            print("OOps... Hubo un error conectando a PostgreSQL")
    
    def desconectar(self):
        try:
            if self.conexion:
                self.conexion.close()
        except:
            print("OOps... Hubo un error desconectando de PostgreSQL")

    def cargarCSV(self):
        self.conectar()
        tt = {}
        try:

            # fich = input("Introduzca el nombre del fichero con la extensión: ")
            fich = "res.partner.csv"
            with open(fich, newline='') as ficheroCSV:
                reader = DictReader(ficheroCSV)
                print("leyendo datos...")
                clave = 1
                for row in reader:
                    tt[clave]=Usuario(row['Nombre'],row['NombreMostrado'],row['Contacto'],row['Direccion'],row['Telefono'],row['Correo'],row['Web'],row['Ciudad'],row['CP'],row['Tipo'],row['Active'])
                    # print(tt.get(clave).tipo)
                    clave=clave+1
            # print(tt.get(1).usuario, tt.get(1).contrasena)
            # tup = tt.items()
            # print(tabulate(tup, headers='firstrow', tablefmt='psql', stralign='left' ))
            rpta = input("\n\n¿Desea introducir estos datos en la tabla de Odoo? S/N: ")
            if rpta.upper() == "S":
                self.csvAtabla(tt)
            else:
                kk = input("\nNo se cargaron datos en la tabla\n\tPulse una tecla para continuar...")
        except:
            self.desconectar
            print("OOps... Se ha encontrado un problema cargando el archivo '{}'".format(fich))
        finally:
            self.desconectar()    

    def csvAtabla(self, datos):
        # self.conectar()
        actualizados = 0
        insertados = 0

        try:
            for us in datos.values():
                if self.buscarUsuario(us):
                    actualizados = actualizados + 1
                    self.accionSql(us, True)
                else:
                    insertados = insertados + 1
                    self.accionSql(us, False)
            print("\n\nResultado --------------------\n\t{} registros fueron actualizados\n\t{} registros nuevos fueron insertados".format(actualizados, insertados))
            # self.desconectar()
        except:
            print("OOps... Hubo un problema en el triaje")
            pass

    def accionSql(self, us, o):
            # self.conectar()
        cur = self.conexion.cursor()
        try:
            if (o == True):
                sql = "UPDATE RES_PARTNER SET NAME='{}', display_name='{}', STREET='{}', PHONE='{}', EMAIL='{}', WEBSITE='{}', CITY='{}', ZIP='{}', ACTIVE='{}' WHERE NAME = '{}'".format(us.nombre,us.nombreMostrado,us.direccion,us.telefono,us.correo,us.web,us.ciudad,us.cp,us.active,us.nombre)
            else:
                sql = '''INSERT INTO RES_PARTNER (NAME, display_name, STREET, PHONE, EMAIL, WEBSITE, CITY, ZIP, ACTIVE) VALUES('{}','{}','{}','{}','{}','{}','{}','{}','{}');
                '''.format(us.nombre,us.nombreMostrado,us.direccion,us.telefono,us.correo,us.web,us.ciudad,us.cp,us.active)
                cur.execute(sql)
                self.conexion.commit()
                if (self.buscarUsuario(us)):
                    sql = "SELECT ID FROM RES_PARTNER WHERE NAME = '{}';".format(us.nombre)
                    cur.execute(sql)
                    idid = cur.fetchone()
                    # print(idid[0])
                    if us.tipo == "T":
                        cat = 9
                    elif us.tipo == "C":
                            cat = 8
                    elif us.tipo == "P":
                            cat = 1
                    else:
                        print("La categoria cargada es incorrecta")
                    sql = "insert into res_partner_res_partner_category_rel (partner_id, category_id) values({},{})".format(idid[0],cat)
                    cur.execute(sql)
                    self.conexion.commit()
            # self.desconectar()
            pass
        except:
            print("OOps... Hubo un error al intentar cargar los usuarios en la tabla")
            pass

    def listarContactos(self):
        self.conectar()
        try:
            # sql= "SELECT ID, NAME, display_name, STREET, PHONE, EMAIL, WEBSITE, CITY, ZIP, TYPE FROM RES_PARTNER ORDER BY ID;"
            sql = '''select f1.id as ID, f1.display_name as Cliente, f1.name as Contacto, street as Dirección, phone As Teléfono, email as Correo, city as Población, zip as CP, 
            CASE WHEN f3.id=1 THEN 'P'
            WHEN f3.id=8 THEN 'C'
            WHEN f3.id=9 THEN 'T'
            END As Tipo, f3.id as F3ID
            from res_partner f1, res_partner_res_partner_category_rel f2, res_partner_category f3
            where (f1.id=f2.partner_id or f1.parent_id=f2.partner_id) and f2.category_id=f3.id and f3.id in (1,8,9)
            order by f1.name;'''
            cur = self.conexion.cursor()
            cur.execute(sql)
            consulta = cur.fetchall()
            resultado = [["Id", "Cliente", "Contacto", "Direccion", "Telefono", "Correo", "Poblacion", "CP", "Tipo", "F3 ID"]]
            for (f1_id, f1_display_name, f1_name, street, phone, email, city, zip, f3_id, f3id) in consulta:
                resultado.append([f1_id, f1_display_name, f1_name, street, phone, email, city, zip, f3_id, f3id])

            # resultado = [["Id", "Nombre", "Nombre Mostrado", "Direccion", "Telefono", "Correo", "Web", "Ciudad", "CP", "Tipo"]]
            # for (ID, NAME, display_name, STREET, PHONE, EMAIL, WEBSITE, CITY, ZIP, TYPE) in consulta:
            #     resultado.append([ID, NAME, display_name, STREET, PHONE, EMAIL, WEBSITE, CITY, ZIP, TYPE])
            print(tabulate(resultado, headers='firstrow', tablefmt='psql', stralign='left'))
        except:
            print("OOps... Hubo algún problema listando los contactos")
            pass
        finally:
            self.desconectar()

    def modificarContacto(self):
            self.conectar()
            claveId = input("Introduzca el 'id' del usuario que desea modificar: ")
            datos = ["Nombre y Apellidos", "Nombre Mostrado", "Direccion", "Teléfono", "Correo", "Web", "Ciudad", "C.P."]
            dicDatos = {}
        # try:
            sql= "SELECT NAME, display_name, STREET, PHONE, EMAIL, WEBSITE, CITY, ZIP FROM RES_PARTNER WHERE ID = '{}';".format(claveId)
            cur = self.conexion.cursor()
            cur.execute(sql)
            consulta =cur.fetchone()
            if cur.rowcount == 0:
                print("No se ha encontrado ningún usuario con la id = {} en la base de datos".format(claveId))
            else:
                c = 0
                for d in datos:
                    dicDatos[d]= input("Introduzca el {} del contacto: ({}) ".format(d,consulta[c]))
                    c = c + 1
                cat = input("Introduzca el , 'Tipo (C(8),P(1) ó T(9))' del contacto: ")
            sql = "UPDATE RES_PARTNER SET NAME='{}', display_name='{}', STREET='{}', PHONE='{}', EMAIL='{}', WEBSITE='{}', CITY='{}', ZIP='{}' WHERE ID = '{}'".format(dicDatos.get(datos[0]),dicDatos.get(datos[1]),dicDatos.get(datos[2]),dicDatos.get(datos[3]),dicDatos.get(datos[4]),dicDatos.get(datos[5]),dicDatos.get(datos[6]),dicDatos.get(datos[7]),claveId)
            cur.execute(sql)
            sql = "update res_partner_res_partner_category_rel set partner_id='{}', category_id='{}' where partner_id='{}'".format(claveId,cat,claveId)
            cur.execute(sql)
            self.conexion.commit()
        # except:
        #     print("OOps... Hubo algún problema actualizando al usuario")
        #     pass
        # finally:
            self.desconectar()

    def detalleContacto(self):
        self.conectar()
        claveId = input("Introduzca el 'id' del usuario deseado: ")
        try:
            # sql= "SELECT ID, NAME, display_name, STREET, PHONE, EMAIL, WEBSITE, CITY, ZIP, TYPE FROM RES_PARTNER WHERE ID = '{}';".format(claveId)
            sql = '''select f1.id as ID, f1.display_name as Cliente, f1.name as Contacto, street as Dirección, phone As Teléfono, email as Correo, city as Población, zip as CP, 
            CASE WHEN f3.id=1 THEN 'P'
            WHEN f3.id=8 THEN 'C'
            WHEN f3.id=9 THEN 'T'
            END As Tipo, f3.id as F3ID
            from res_partner f1, res_partner_res_partner_category_rel f2, res_partner_category f3
            where (f1.id=f2.partner_id or f1.parent_id=f2.partner_id) and f2.category_id=f3.id and f3.id in (1,7,8) and f1.id = '{}'
            order by f1.name;'''.format(claveId)
            cur = self.conexion.cursor()
            cur.execute(sql)
            consulta = cur.fetchone()
            if cur.rowcount == 0:
                print("No se ha encontrado ningún usuario con la id = {} en la base de datos".format(claveId))
            else:
                # resultado = [["Id", "Nombre", "Nombre Mostrado", "Direccion", "Telefono", "Correo", "Web", "Ciudad", "CP", "Tipo"]]
                # resultado.append([consulta[0],consulta[1],consulta[2],consulta[3],consulta[4],consulta[5],consulta[6],consulta[7],consulta[8],consulta[9]])

                resultado = [["Id", "Cliente", "Contacto", "Direccion", "Telefono", "Correo", "Poblacion", "CP", "Tipo", "F3 id"]]
                resultado.append([consulta[0],consulta[1],consulta[2],consulta[3],consulta[4],consulta[5],consulta[6],consulta[7],consulta[8],consulta[9]])
                print(tabulate(resultado, headers='firstrow', tablefmt='psql', stralign='left'))
        except:
            print("OOps... Hubo algún problema buscando al usuario")
            pass
        finally:
            self.desconectar()
        
    def buscarUsuario(self, u):
        # self.conectar()
        try:
            sql= "SELECT NAME FROM RES_PARTNER WHERE NAME = '{}';".format(u.nombre)
            cur = self.conexion.cursor()
            cur.execute(sql)
            if cur.rowcount == 0:
                salida = False
            else:
                salida = True
            
            # self.desconectar()
            return salida
        except:
            print("OOps... Hubo algún problema buscando al usuario")
            pass