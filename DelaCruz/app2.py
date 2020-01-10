import libreria

opc=0
max=4
while (opc!=max):
	print("################# MENU ##################")
	print ("#######  Selecciona una opción  ########")
	print ("# 1. primera opción (Play)             #")
	print ("# 2. segunda opción (1 jugador)        #")
	print ("# 3. tercera opción(2 o mas jugadores) #")
	print ("# 4. salir                             #")
	print("#########################################")
	opcionMenu=libreria.pedir_numero("inserta la opcion que desees: ", 1,4)


	if (opcionMenu==1):
		print ("")
		input("Has pulsado la opción 1. Play...\npulsa una tecla del 1 al 4 para continuar")
	if opcionMenu==2:
		print ("")
		input("Has pulsado la opción 2. 1 jugador...\npulsa una tecla del 1 al 4 para continuar")
	if opcionMenu==3:
		print ("")
		input("Has pulsado la opción 3. 2 o mas jugadores...\npulsa una tecla del 1 al 4 para continuar")
	if opcionMenu==4:
		break
	else:
		print ("")
		input("No has pulsado ninguna opción correcta...\npulsa una tecla del 1 al 4 para continuar")
