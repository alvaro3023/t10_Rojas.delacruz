import libreria
#1. Implementacion de submenu
def pedirRUC():
    RUC=libreria.pedir_numero("El RUC es:", 1, 100000000000)
    print ("Se agrego el RUC")
    libreria.guardar_datos("ruc.txt", contenido , "a")
    print ("Datos guardados")
def mostrarmonto():
    monto=libreria.pedir_numero("El monto es:"10, 300)
    print ("Se agrego el monto")
# Menu de comandos
opc=0
max=3
while(opc!= max):
    print("############### MENU ##############")
    print("#1. pedir RUC  ")
    print("#2. Mostrar monto")
    print("#3. Salir")
    #2. Eleccion de la opcion menu
    opc=libreria.pedir_numero("Ingreso la opcion:", 1, 3)
    #3. Mapeo de las opciones
    if (opc==1):
        pedirRUC()
    if (opc==2):
        mostrarmonto()

    #fin_while
