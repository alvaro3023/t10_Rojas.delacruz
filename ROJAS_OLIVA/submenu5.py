import libreria
#1. Implementacion de submenu
def opcionapertura():
    dia=libreria.pedir_dia("El dia es:", 1, 31)
    mes=libreria.pedir_mes("El mes es:", 1, 12)
    anio=libreria.pedir_anio("El año es:", 1, 3000)
    print("LA APERTURA ES :", str(dia) + "/" + str(mes) + "/" + str(_anio))

def opcionnacimiento():
    fecha=libreria.pedir_anio("EL AÑO DE NACIMIENTO ES:",1990, 2 200)
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
