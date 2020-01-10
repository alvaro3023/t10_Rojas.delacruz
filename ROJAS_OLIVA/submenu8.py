import libreria
#1. Implementacion de submenu
def opcionfuerzaelast():
    x=libreria.pedir_numero("La deformacion es:", 1, 50)
    k=libreria.pedir_numero("La constante elastica:", 20, 30)
    print ("La fuerza elastica es:", (k)*(x**2)/2)
def opcionvariaciont():
    Ti=libreria.pedir_booleano("La T inicial es:", 2.5, 100.5)
    Tf=libreria.pedir_booleano("La T final es:", 204.75, 390.45)
    print ("La variacion de la temperatura es:", Tf-Ti)

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
