# encoding: utf-8

import os

vida = 3

def limpiarP():
    os.system("clear")


def ObjetosCocina(vida):

    objetos_cocina = ["platos", "tenedores", "cucharas","hoyas", "nevera", "comedor","mesa", "vasos"]

    volverAIntentar = True
    while volverAIntentar == True:
        limpiarP()

        print " -------------------------------------------------------------------------------"
        print " ==========================|   OBJETOS DE COCINA    |==========================="
        print " -------------------------------------------------------------------------------"
        print " DIVINA LOS OBJETOS DE UNA COCINA: \n"
        print " Objetos restantes:", len(objetos_cocina)
        print " Vida:", vida

        palabra = raw_input("\n ¿Que objetos se encuentran en una cocina?: ")
        palabra = palabra.lower()

        if palabra in objetos_cocina:
            objetos_cocina.remove(palabra)

            if len(objetos_cocina) == 0:
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
