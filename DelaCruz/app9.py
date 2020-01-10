import libreria

def ingrese_frutas():
    input("Ingrese frutas: ")

def ingrese_postres():
    input("Ingrese postres: ")

def ingrese_jugos():
    input("Ingrese jugos: ")


opc=0
max=4
while(opc!=max):
    print("########## TIENDA ##########")
    print("#1. Frutas                 #")
    print("#2. Postres                #")
    print("#3. Jugos                  #")
    print("#4. Salir                  #")
    print("############################")

    opc=libreria.pedir_numero("ingrese opcion:", 1, 4)

    if (opc==1):
        ingrese_frutas()
    if (opc==2):
        ingrese_postres()
    if (opc==3):
        ingrese_jugos()

print("Fin del programa")
