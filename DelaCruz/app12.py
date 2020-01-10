import libreria
def pedir_sandia():
    libreria.pedir_fruta("ingrese fruta:")
    print("Se ingreso la fruta")


def pedir_melon():
    print("Se agreo la fresa")
def pedir_mandarina():
    print("se agrego mandarina")
def pedir_tomate():
    print("se agrego tomate")
def pedir_brocoly():
    print("se agrego el brocoly")
def pedir_zanahoria():
    print("Se agrego zanahoria")
def pedir_cebolla():
    print("se agrego cebolla")

def agregar_fruta():

    opc=0
    max=4
    while(opc!=max):
       print("##### menu-frutas #####")
       print("# 1.- sandia          #")
       print("# 2.- melon           #")
       print("# 3.- mandarina       #")
       print("# 4.-salir            #")
       print("#######################")

       opc=libreria.pedir_numero("ingrese opcion:",1,4)

       if(opc==1):
           pedir_platano()
       if(opc==2):
           pedir_fresa()
       if(opc==3):
           pedir_mandarina()


def agregar_verdura():
    opc=0
    max=5
    while(opc!=max):
       print("####sub-menu-verduras####")
       print("# 1.- tomate            #")
       print("# 2.- brocoly           #")
       print("# 3.- zanahoria         #")
       print("# 4.- cebolla           #")
       print("# 5.- salir             #")
       print("#########################")
       opc=libreria.pedir_numero("ingrese opcion:",1,5)

    if(opc==1):
        pedir_tomate()
    if(opc==2):
        pedir_brocoly()
    if(opc==3):
        pedir_zanahoria()
    if(opc==4):
        pedir_cebolla()


opc=0
max=3
while(opc!=3):
    print("########### MENU #############")
    print("# 1. Fruta                   #")
    print("# 2. Verdura                 #")
    print("# 3. salir                   #")
    print("##############################")

    opc=libreria.pedir_numero("ingrese opcion:",1,3)

    if(opc==1):
        agregar_fruta()
    if(opc==2):
        agregar_verdura()

print("Programa finalizado")
# fin de menu
