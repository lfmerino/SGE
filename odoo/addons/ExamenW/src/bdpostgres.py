#!/user/bin/env python 
# -*- coding: utf-8 -*-

import psycopg2

class BD:
    conexion = None
    puntero = None
    
    def __init__(self):
        self.conexio = None
        self.puntero = None
        
    def CrearConexion(self,bd,u,h,psw,p):
        try:
            self.conexion = psycopg2.connect(dbname=bd, user=u, host=h, password=psw, port=p)
            self.puntero = self.conexion.cursor()
        except ValueError:
            print("Error de conexión")
        
    def CerrarConexion(self):
        self.puntero.close()
        self.conexion.close()

    def ConsultaDic(self,sentencia):
#puntero = self.conexion.cursor()
        try:
            self.puntero.execute(sentencia)
            if sentencia.upper().startswith('SELECT'):
                return self.puntero.fetchall()
            else:
                self.conexion.commit()
        except Exception:
            print('Error al ejecutar sentencia')
            print(sentencia)
#puntero.execute(sentencia)
pass
#self.conexion = psycopg2.connect(dbname=self.bd, user=self.u, host=self.h, password=self.psw, port=self.p)

