import libreria
opc=0
max=3
def agregar_nombre():
    input("Agregar nombre del docente: ")

def agregar_curso():
    input("Agregar curso que enseña: ")


while (opc!=max):
    print("########## MENU #############")
    print("#1. Docente:                #")
    print("#2. Curso:                  #")
    print("#3. Salir                   #")
    print("#############################")
    opc=libreria.pedir_numero("Ingrese opcion:", 1,3)

# Mapeo de funciones
    if(opc==1):
        agregar_nombre()
    if(opc==2):
        agregar_curso()

print("Fin del programa")
