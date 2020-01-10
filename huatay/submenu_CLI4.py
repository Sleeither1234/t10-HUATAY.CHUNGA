def on():
    def potencia():
        print("REGULE la potencia del dinamo")
        ingresa=input("POr favor ingrese el porcentaje que desea del dinamo")
        archivo=open("dinamo.txt","w")
        archivo.write("EL nivel del dinamo esta al "+ingresa)
        archivo.close()
    def color():
        a="1)rojo"
        b="2)amarillo"
        c="3)violeta"
        d="4)azul"
        lista=[a,b,c,d]
        elejir=int(input("ingrese su opcion"))
        if elejir==1:
            print("usted ha elejido el color "+a)
            archivo=open("color.txt","w")
            archivo.write("El color del dinamo es: "+a)
            archivo.close()
        if elejir==2:
            print("usted ha elejido el color "+b)
            archivo=open("color.txt","w")
            archivo.write("El color del dinamo es: "+b)
            archivo.close()
        if elejir==3:
            print("usted ha elejido el color "+c)
            archivo=open("color.txt","w")
            archivo.write("El color del dinamo es: "+c)
            archivo.close()
        if elejir==4:
            print("usted ha elejido el color "+c)
            archivo=open("color.txt","w")
            archivo.write("El color del dinamo es: "+d)
            archivo.close()
        else:
            print("comando no seleccionado")
    opc=0
    max=3
    while opc!=max:
        print("#EL DINAMO SE HA PRENDIDO######")
        print("#1.potencia                   #")
        print("#2.color                      #")
        print("#3.Salir                      #")
        print("###############################")
        opc=libreria.validar_menu(input("Inngrese su opcion"))
        if opc==1:
            potencia()
        elif opc==2:
            color()
def Estado():
    def parametros():
        porcentaje = libreria.validar_menu("Ingres el porcentaje del dinamo")
        color = libreria.validar_apellido(input("Ingrese el nombre del color"))
        archivo = open("parametros.txt", "w")
        archivo.write("DINAMO" + "\n" + "PORCENTAJE: " + str(porcentaje) + "\n" + "COLOR: " + color)
        archivo.close()
    def color():
        porcentaje = libreria.validar_suma(input("Ingrese el numero"))
        if porcentaje > 75 and porcentaje < 100:
            print("tiene usted buena iluminacion")
        if porcentaje > 25 and porcentaje < 75:
            print("Tiene una Iluminacion regular")
        if porcentaje <= 25 and porcentaje > 0:
            print("Tiene una baja iluminacion")


    opc = 0
    max = 3
    while opc!=max:

        print("#EL ESTADO DEL DINAMO #########")
        print("#1.Parametros                 #")
        print("#2.DATOS DE WHAPS             #")
        print("#3.Salir                      #")
        print("###############################")
        opc = libreria.validar_menu(input("Inngrese su opcion"))
        if opc == 1:
            parametros()
        elif opc == 2:
            color()


import libreria
opc=0
max=3
while opc!=max:
    print("##########dinamo#############")
    print("#1.On                       #")
    print("#2.Estado                   #")
    print("#3.Oof                      #")
    print("#############################")
    opc=libreria.validar_menu(input("Ingrese su opcion "))
    if opc==1:
        on()
    if opc==2:
        Estado()
