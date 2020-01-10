import libreria
opc=0
max=3
def agregar_nombre():
    input("Ingrese Nombre: ")

def agregar_apellido():
    input("Ingrese almuerzo: ")


while (opc!=max):
    print("########## MENU #############")
    print("#1. Desayuno:               #")
    print("#2. Almuerzo:               #")
    print("#3. Salir                   #")
    print("#############################")
    opc=libreria.pedir_numero("Ingrese opcion:", 1,3)

# Mapeo de funciones
    if(opc==1):
        agregar_nombre()
    if(opc==2):
        agregar_apellido()

print("Fin del programa")
