import libreria
#1. Implementacion de submenu
def opccionmultiplicar():
    n1=libreria.pedir_numero("El N1 es:", 1, 100)
    n2=libreria.pedir_numero("El N2 es:", 1, 100)
    print("La multiplicacion es:", n1*n2 )
def restardosnumeros():
    n1=libreria.pedir_numero("El N1 es:", 1, 100)
    n2=libreria.pedir_numero("El N2 es:", 1, 100)
    print("La division es:", n1/n2)

# Menu de comandos
opc=0
max=3
while(opc!= max):
    print("############### MENU ##############")
    print("#1. Multiplicar dos numeros  ")
    print("#2. Dividir dos numeros")
    print("#3. Salir")
    #2. Eleccion de la opcion menu
    opc=libreria.pedir_numero("Ingreso la opcion:", 1, 3)
    #3. Mapeo de las opciones
    if (opc==1):
        opcionmultiplicar()
    if (opc==2):
        opciondivir()

    #fin_while

