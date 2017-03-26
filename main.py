from objetos_cocina import *
from objetos_sala import *


menu = True
while menu == True:
	limpiarP()
	print " -------------------------------------------------------------------------------"
	print " ===========================|   ADIVINAR OBJETOS    |==========================="
	print " -------------------------------------------------------------------------------"
	print " |       (1) OBJETOS DE COCINA          |        (2) OBJETOS DE UNA SALA       |"
	print " -------------------------------------------------------------------------------"
	print " |       (3) OBJETOS DE                 |        (4) OBJETOS DE                |"
	print " -------------------------------------------------------------------------------"
	print " |                             |   (0) SALIR    |                              |"
	print " -------------------------------------------------------------------------------"

	try:
		print
		opcion = int(input(" Opcion > "))

	except:
		print
		print "                               'Opcion invalida'"
		print "                         Presione ENTER para continuar"
		print
		raw_input()
		continue

	if opcion == 0:
		print "\n 'Ha salido del juego' \n"
		break

	elif opcion == 1:
		volverAIntentar = True

		while volverAIntentar == True:
			ObjetosCocina(vida)

			print
			print " (v) Volver al menu principal"
			print " (i) Volver a intentar"
			print " (s) Salir del juego"

			elegir = raw_input("\n Opcion > ")

			if elegir == 's':
				print "\n 'Ha salido del juego' \n"
				volverAIntentar = False
				menu = False

			if elegir == 'v':
				volverAIntentar = False
				menu = True

	        if elegir == 'i':
	          	volverAIntentar = True

	elif opcion == 2:
		volverAIntentar = True

		while volverAIntentar == True:
			ObjetosSala(objetos_sala,vida)

			print
			print " (v) Volver al menu principal"
			print " (i) Volver a intentar"
			print " (s) Salir del juego"

			elegir = raw_input("\n Opcion > ")

			if elegir.lower() == 's':
				print "\n 'Ha salido del juego' \n"
				volverAIntentar = False
				menu = False

			if elegir.lower() == 'i':
				volverAIntentar = True

			if elegir.lower() == 'v':
				volverAIntentar = False
				menu = True







        



