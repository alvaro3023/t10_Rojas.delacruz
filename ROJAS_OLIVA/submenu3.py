import libreria
#1. Implementacion de submenu
def opcionareatriangulo():
    base=libreria.pedir_numero("La base es:", 10 , 50)
    altura=libreria.pedir_numero("La altura es:", 5, 25)
    print ("La area del triangulo es:", base*altura/2)
def opcionareatrapecio():
    B=libreria.pedir_numero("La base mayor es:", 10, 20)
    b=libreria.pedir_numero("La base menor es:", 1, 9 )
    h=libreria.pedir_numero("La altura es:", 5, 10)
    print ("El area del trapecio es:", ((b + b)/2)*h )


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
