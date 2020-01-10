import libreria
opc=0
max=3
def agregar_uni():
    input("Ingresar universidad: ")

def agregar_carrera():
    input("Ingresar carrera profesional: ")


while (opc!=max):
    print("########## MENU #############")
    print("#1. Universidad             #")
    print("#2. Carrera profesion       #")
    print("#3. Salir                   #")
    print("#############################")
    opc=libreria.pedir_numero("Ingrese opcion:", 1,3)

# Mapeo de funciones
    if(opc==1):
        agregar_uni()
    if(opc==2):
        agregar_carrera()


print("Fin del programa")
