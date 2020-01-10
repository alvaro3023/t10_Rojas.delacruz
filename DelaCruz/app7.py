import libreria
opc=0
max=3
def agregar_hotel():
    input("Ingrese nombre del hotel: ")

def agregar_nro_habitacion():
    input("Ingrese numero de habitacion: ")


while (opc!=max):
    print("########## MENU #############")
    print("#1. Hotel:                  #")
    print("#2. N° habitacion:          #")
    print("#3. Salir                   #")
    print("#############################")
    opc=libreria.pedir_numero("Ingrese opcion:", 1,3)

# Mapeo de funciones
    if(opc==1):
        agregar_hotel()
    if(opc==2):
        agregar_nro_habitacion()

print("Fin del programa")
