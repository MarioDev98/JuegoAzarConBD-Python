import mysql.connector
import random
import datetime

class Metodos:

    def __init__(self):
        self.conn = mysql.connector.connect(host='la ip o localhost',
                             user='el usario',
                             passwd='contrasena del usuario',
                             db='nombre de la base de datos')
        self.cursor=self.conn.cursor()

    def Consulta(self):
        # sqlread="SELECT * FROM random"
        self.cursor.execute("SELECT * FROM random")
        jugadores = self.cursor.fetchall()
        for jugadore in jugadores:
            print(jugadore)
        

    def Create(self):
        numero=random.randrange(1,1000)
        # print(numero)
        nombre = input("\nIngresas es tu nombre: ")
        correo = input("Ingresa tu correo electronico: ")
        edad = int(input("Ingresa tu edad : "))
        respuesta=int(input('Dime el número que he elegido: '))
        contador = 0
        fecha_incio=datetime.datetime.now()
        while respuesta!=numero:
            contador=contador+1
            if respuesta>numero:
                respuesta=int(input('El número que buscas es  mas pequeño al que ingresaste : '))
            elif respuesta<numero:
                respuesta=int(input('El número que buscas  es mas grande al que ingresaste : '))
        print("\nFelicidades tienes el menor numero, ahora eres el recor a superar")
        # print('Has adivinado que el número correcto es:',numero,"intentos", contador, "\n")
        fecha_final=datetime.datetime.now()
        
        # sql = "INSERT INTO random(nombre,correo,edad,intetos) VALUES('{}')".format(nombre,correo,edad,contador)
        self.cursor.execute("INSERT INTO random(nombre,correo,edad,time_inicio,time_fin,intentos) VALUES('{}','{}','{}','{}','{}','{}')".format(nombre,correo,edad,fecha_incio,fecha_final,contador))
        print("\nIngresado correctamente a la base de datos")
        self.conn.commit()
        
pruebas = Metodos()
pruebas.Consulta()
pruebas.Create()

#La librerias importadas fueron
# pip install mysql.connector