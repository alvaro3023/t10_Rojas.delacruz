import libreria
def pedir_gelatina():
    libreria.pedir_postre("ingrese postre:")
    print("Se ingreso el postre")

def pedir_flan():
    print("Se agreo el flan")
def pedir_torta():
    print("se agrego torta tres leche")


def pedir_fresa():
    libreria.pedir_jugo("ingrese jugo:")
    print("Se agrego jugo de fresa")
def pedir_platano():
    print("Se agrego jugo de platano")
def pedir_papaya():
    print("Se agrego jugo de papaya")



def agregar_fruta():

    opc=0
    max=4
    while(opc!=max):
       print("##### menu-Postres #########")
       print("# 1.- Gelatina             #")
       print("# 2.- Flan                 #")
       print("# 3.- Torta tres leches    #")
       print("# 4.-salir                 #")
       print("############################")

       opc=libreria.pedir_numero("ingrese opcion:",1,4)

       if(opc==1):
           pedir_gelatina()
       if(opc==2):
           pedir_flan()
       if(opc==3):
           pedir_torta()

def pedir_fresa():
    libreria.pedir_jugo("ingrese jugo:")
    print("Se agrego jugo de fresa")
def pedir_platano():
    print("Se agrego jugo de platano")
def pedir_papaya():
    print("Se agrego jugo de papaya")

def agregar_jugos():
    opc=0
    max=4
    while(opc!=max):
       print("####sub-menu-Jugos####")
       print("# 1.- Platano           #")
       print("# 2.- Papaya            #")
       print("# 3.- Fresa             #")
       print("# 4.- salir             #")
       print("#########################")
       opc=libreria.pedir_numero("ingrese opcion:",1,4)

    if(opc==1):
        pedir_platano()
    if(opc==2):
        pedir_papaya()
    if(opc==3):
        pedir_fresa()


opc=0
max=3
while(opc!=3):
    print("########### MENU #############")
    print("# 1. Postre                  #")
    print("# 2. Jugos                   #")
    print("# 3. salir                   #")
    print("##############################")

    opc=libreria.pedir_numero("ingrese opcion:",1,3)

    if(opc==1):
        agregar_fruta()
    if(opc==2):
        agregar_jugos()

print("Programa finalizado")
# fin de menu
