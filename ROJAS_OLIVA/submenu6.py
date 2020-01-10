import libreria
#1. Implementacion de submenu
def opciontadecuada():
    temperatura_adecuada=libreria.pedir_entero("LA T° adecuada es:", 10 , 20)
    print("LA T° es:", temperatura_adecuada)
def opciontexcesiva():
    t_excesiva=libreria.pedir_entero("La T° excesiva es:", 21, 50)
    print ("La T° excesiva es:", t_excesiva)
# Menu de comandos
opc=0
max=3
while(opc!= max):
    print("############### MENU ##############")
    print("#1. Temperatura adecuada")
    print("#2. Temperatura excesiva")
    print("#3. Salir")
    #2. Eleccion de la opcion menu
    opc=libreria.pedir_numero("Ingreso la opcion:", 1, 3)
    #3. Mapeo de las opciones
    if (opc==1):
        opciontadecuada()
    if (opc==2):
        opciontexcesiva()
