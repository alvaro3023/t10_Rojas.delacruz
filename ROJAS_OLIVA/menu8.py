# Menu de comandos
opc=0
max=3
while(opc!= max):
    print("############### MENU ##############")
    print("#1. Mostrar fuerza elastica  ")
    print("#2. Mostrar variacion de temperatura ")
    print("#3. Salir")
    #2. Eleccion de la opcion menu
    opc=libreria.pedir_numero("Ingreso la opcion:", 1, 3)
    #3. Mapeo de las opciones
    if (opc==1):
        opcionfuerzaelast()
    if (opc==2):
        opcionvariaciont()
