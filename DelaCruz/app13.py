import libreria
def pedir_platano():
    libreria.pedir_uni("ingrese universidad:")
    print("Se ingreso la universidad")


def pedir_UNPRG():
    print("Se agreo la UNPRG ")
def pedir_USAT():
    print("se agrego USAT ")
def pedir_UTP():
    print("se agrego UTP")

def agregar_uni():

    opc=0
    max=4
    while(opc!=max):
       print("##### menu-universidades #####")
       print("# 1.- UNPRG          #")
       print("# 2.- USAT           #")
       print("# 3.- UTP            #")
       print("# 4.-salir            #")
       print("#######################")

       opc=libreria.pedir_numero("ingrese opcion:",1,4)

       if(opc==1):
           pedir_UNPRG()
       if(opc==2):
           pedir_USAT()
       if(opc==3):
           pedir_UTP()


opc=0
max=3
while(opc!=2):
    print("########### MENU #############")
    print("# 1. Universidades           #")
    print("# 2. salir                   #")
    print("##############################")

    opc=libreria.pedir_numero("ingrese opcion:",1,3)

    if(opc==1):
        agregar_uni()

print("Programa finalizado")
# fin de menu
