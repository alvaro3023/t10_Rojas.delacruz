# Menu de comandos
opc=0
max=3
while(opc!= max):
    print("############### MENU ##############")
    print("#1. Mostrar area del circulo ")
    print("#2. Mostrar area cuadrado ")
    print("#3. Salir")
    #2. Eleccion de la opcion menu
    opc=libreria.pedir_numero("Ingreso la opcion:", 1, 3)
    #3. Mapeo de las opciones
    if (opc==1):
        opcionareacirculo()
    if (opc==2):
        opcionareacuadrado()

    #fin_while
