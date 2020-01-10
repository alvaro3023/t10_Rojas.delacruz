# Menu de comandos
opc=0
max=3
while(opc!= max):
    print("############### MENU ##############")
    print("#1. Mostrar dia de apertura   ")
    print("#2. Mostrar año de nacimiento")
    print("#3. Salir")
    #2. Eleccion de la opcion menu
    opc=libreria.pedir_numero("Ingreso la opcion:", 1, 3)
    #3. Mapeo de las opciones
    if (opc==1):
        opcionapertura()
    if (opc==2):
        opcionnacimiento()

    #fin_while
