def validar_entero(n):
    if (isinstance(n, int)):
        return True
    else:
        return False

def validar_rango(n, ri, rf):
    if ( validar_entero(n) == True):
        if (n >= ri and n <= rf):
            return True
        else:
            return False
    else:
        return False

def pedir_numero(msg, ri, rf):
    n=""
    while( validar_rango(n, ri, rf) == False):
       n=input(msg)
       if ( n.isdigit() == True):
           n = int(n)
    #fin_while
    return n
#fin_pedir_numero

def validar_nombre(nombre):
    if ( isinstance(nombre, str)):
        if (len(nombre) >= 3):
            return True
        else:
            return False
    else:
        return False

def pedir_nombre(msg):
    nombre=""
    while ( validar_nombre(nombre) == False ):
        nombre=input(msg)
    #fin_while
    return nombre
#fin_pedir_nombre

def guardar_datos(nombre_archivo, contenido, modo):
    archivo=open(nombre_archivo, modo)
    archivo.write(contenido)
    archivo.close()

def obtener_datos(nombre_archivo):
    archivo=open(nombre_archivo)
    contenido = archivo.read()
    archivo.close()
    return contenido

def pedirNumeroEntero():

    correcto=False
    num=0
    while(not correcto):
        try:
            num = int(input("Introduce un numero entero: "))
            correcto=True
        except ValueError:
            print('Error, introduce un numero entero')

    return num

def validar_postres(nombre):
    if ( isinstance(nombre, str)):
        if (nombre=="Torta tres leches" and nombre=="Gelatina" and nombre=="Flan"):
            return True
        else:
            return False
    else:
        return False

def  pedir_postre(nombre):

    postre=""
    while(validar_postres==False):
        fruta=input(nombre)
    return fruta

def validar_jugos(msg):
    if ( isinstance(msg, str)):
        if (msg=="Papaya" and msg=="Platano" and msg=="Fresa"):
            return True
        else:
            return False
    else:
        return False

def  pedir_jugos(msg):

    jugos=""
    while(validar_jugos==False):
        jugos=input(msg)
    return jugos

def validar_frutas(msg):
    if ( isinstance(msg, str)):
        if (msg=="sandia" and msg=="melon" and msg=="mandarina"):
            return True
        else:
            return False
    else:
        return False

def  pedir_frutas(msg):

    fruta=""
    while(validar_frutas==False):
        fruta=input(msg)
    return fruta

def validar_verdura(msg):
    if ( isinstance(msg, str)):
        if (msg=="tomate" and msg=="brocoly" and msg=="zanahoria" and msg=="cebolla"):
            return True
        else:
            return False
    else:
        return False

def  pedir_verduras(msg):

    verdura=""
    while(validar_verduras==False):
        verdura=input(msg)
    return verdura

def validar_uni(msg):
    if ( isinstance(msg, str)):
        if (msg=="UNPRG" and msg=="USAT" and msg=="UTP"):
            return True
        else:
            return False
    else:
        return False

def  pedir_uni(msg):

    UNI=""
    while(validar_uni==False):
        UNI=input(msg)
    return UNI
