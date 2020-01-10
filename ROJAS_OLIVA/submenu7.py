import libreria
#1. Implementacion de submenu
def opciondistancia():
    velocidad=libreria.pedir_numero("La velocidad es:", 1, 1000)
    tiempo=libreria.pedir_numero("El tiempo es:"10, 50)
    print("La distancia es:", velocidad*tiempo)
def opcionarearombo():
    DM=libreria.pedir_numero("La diagonal mayor es:", 5 , 30)
    dm=libreria.pedir_numero("La diagonal menor es:", 5, 10)
    print ("El area del rombo es:", DM*dm/2)
libreria.
# Menu de comandos
opc=0
max=3
while(opc!= max):
    print("############### MENU ##############")
    print("#1. Mostrar la distancia")
    print("#2. Mostrar el area del rombo  ")
    print("#3. Salir")
    #2. Eleccion de la opcion menu
    opc=libreria.pedir_numero("Ingreso la opcion:", 1, 3)
    #3. Mapeo de las opciones
    if (opc==1):
        opciondistancia()
    if (opc==2):
        opcionarearombo()
