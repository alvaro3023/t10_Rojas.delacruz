import libreria
opc=0
max=3
def agregar_prenda():
    input("Ingrese prenda: ")

def agregar_talla():
    input("Ingrese talla: ")


while (opc!=max):
    print("########## MENU #############")
    print("#1. Prenda:                 #")
    print("#2. Talla:                  #")
    print("#3. Salir                   #")
    print("#############################")
    opc=libreria.pedir_numero("Ingrese opcion:", 1,3)

# Mapeo de funciones
    if(opc==1):
        agregar_prenda()
    if(opc==2):
        agregar_talla()

print("Fin del programa")
