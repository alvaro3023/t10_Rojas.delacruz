import libreria
opc=0
max=3
def agregar_dni():
    input("Ingrese DNI: ")


def agregar_clave():
    input("Ingrese clave: ")


while (opc!=max):
    print("############ MENU ###############")
    print("#1. Agregar DNI:                #")
    print("#2. Agregar clave de tarjeta    #")
    print("#3. Salir                       #")
    print("#################################")
    opc=libreria.pedir_numero("Ingrese opcion:", 1,3)

# Mapeo de funciones
    if(opc==1):
        agregar_dni()
    if(opc==2):
        agregar_clave()

print("Fin del programa")
