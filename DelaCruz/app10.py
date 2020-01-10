import libreria
def agregar_fecha1():
    print("Fecha incorrecta ")
    input("Presione cualquier tecla para volver a intentarlo: ")
def agregar_fecha2():
    print("Fecha correcta ")
    input("Presione la opcion 4 si desea salir: ")
def agregar_fecha3():
    print(" Fecha correcta ")
    input("Agregar fecha: ")
opc=0
max=4
while (opc!=max):
    print("################# MENU ##################")
    print("#### Selecciona fecha de cumpleaños #####")
    print("#1. 2 de agosto                         #")
    print("#2. 9 de setiembre                      #")
    print("#3. 19 de julio                         #")
    print("#4. salir                               #")
    print("#########################################")
    opc=libreria.pedir_numero("Ingrese opcion:", 1,4)

    if (opc==1):
        agregar_fecha1()
    if (opc==2):
        agregar_fecha2()
    if (opc==3):
        agregar_fecha3()
    if (opc==4):
        break
