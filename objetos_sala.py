# encoding: utf-8

import os

vida = 3
objetos_sala= ["muebles", "sillas", "jarrones", "lamparas", "adornos", "cogines", "televisor",
			 "fotos"]


def limpiarP():
    os.system("clear")

def ObjetosSala(objetos_sala,vida):

    if len(objetos_sala) == 0:
        objetos_sala= ["muebles", "sillas", "jarrones", "lamparas", "adornos", "cogines", "televisor",
			 "fotos"]

    volverAIntentar = True
    while volverAIntentar == True:
        limpiarP()

        print " -------------------------------------------------------------------------------"
        print " ========================|   OBJETOS DE UNA SALA    |==========================="
        print " -------------------------------------------------------------------------------"
        print " DIVINA LOS OBJETOS DE UNA SALA: \n"
        print " Objetos restantes:", len(objetos_sala)
        print " Vida:", vida

        palabra = raw_input("\n ¿Que objetos se encuentran en una sala?: ")
        palabra = palabra.lower()

        if palabra in objetos_sala:
            objetos_sala.remove(palabra)

            if len(objetos_sala) == 0:
                print "\n GANASTE!!"
                print "\t\t        Haz adivinado todos los objetos!!"
                raw_input()
                volverAIntentar = False

            else:
                print "\n Haz adivinado uno de los objetos!!"
                raw_input()

        else:
            if vida != 0:
                print "\n Objeto incorrecto!!"
                vida -= 1
                raw_input()
                volverAIntentar = True

            else:
                print "\n PERDISTE!!"
                volverAIntentar = False
