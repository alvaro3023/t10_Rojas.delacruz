# Menu de comandos
opc=0
max=3
while(opc!= max):
    print("############### MENU ##############")
    print("#1. agregar area triangulo")
    print("#2. agregar area trapecio ")
    print("#3. salir ")
    #2. Eleccion de la opcion menu
    opc=libreria.pedir_numero("Ingreso la opcion:", 1, 3)
    #3. Mapeo de las opciones
    if (opc==1):
        opcionareatriangulo()
    if (opc==2):
        opcionareatrapecio()


#fin_menu
