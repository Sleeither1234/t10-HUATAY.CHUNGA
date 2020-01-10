def lacteos():
    def yogurt():
        print("Usted ha elejido el producto:"+lacteo)
        anadir=int(input("Desea añadir el producto SI(1) O NO(0)"))
        if anadir==1:
            nombre=libreria.validar_apellido(input("Ingrese su nombre por favor: "))
            archivo=open(nombre+".txt","w")
            archivo.write("Se añadido el producto "+lacteo)
            print("Se guardo correctamente el archivo")
            archivo.close()
        elif anadir==0:
            print("Ok no se guardara el producto")
        else:
            print("El valor inresado es incorrecto ")
    def queso():
        print("Usted ha elejido el producto:" + lacteo1)
        anadir = int(input("Desea añadir el producto SI(1) O NO(0)"))
        if anadir == 1:
            nombre = libreria.validar_apellido(input("Ingrese su nombre por favor: "))
            archivo = open(nombre + ".txt", "w")
            archivo.write("Se añadido el producto " + lacteo1)
            print("Se guardo correctamente el archivo")
            archivo.close()
        elif anadir == 0:
            print("ok no se guardara el producto")
        else:
            print("El valor inresado es incorrecto ")


    opc=0
    max=3
    while opc!=max:
        lacteo="yogurt"
        lacteo1="queso"
        print("##############LACTEOS#############")
        print("#1."+lacteo+"                    #")
        print("#2."+lacteo1+"                   #")
        print("#3.salir                         #")
        print("##################################")
        opc=libreria.validar_menu(input("Ingrese su opcion"))
        if opc==1:
            yogurt()
        if opc==2:
            queso()

def carnes():
    def pollo():
        print("Uste a elejido el producto: "+carne)
        anadir=int(input("DESEA AÑADIR EL PRODUCTO? SI(1) NO (0)"))
        if anadir==1:
            nombre=libreria.validar_apellido(input("Ingrese su nombre por favor: "))
            archivo=open(nombre+".txt","w")
            archivo.write("Se añadido el producto "+carne)
            print("Se guardo correctamente el archivo")
            archivo.close()
        elif anadir==0:
            print("ok no se guardara ningun dato")
        else:
            print("El valor inresado es incorrecto ")

    def pescado():
        print("Uste a elejido el producto: " + carne1)
        anadir = int(input("DESEA AÑADIR EL PRODUCTO? SI(1) NO (0)"))
        if anadir == 1:
            nombre = libreria.validar_apellido(input("Ingrese su nombre por favor: "))
            archivo = open(nombre + ".txt", "w")
            archivo.write("Se añadido el producto " + carne1)
            print("Se guardo correctamente el archivo")
            archivo.close()
        elif anadir == 0:
            print("OK no se guardara el producto")
        else:
            print("El valor inresado es incorrecto ")
    opc=0
    max=3
    carne="pollo"
    carne1="pescado"
    while opc!=max:

        print("############CARNES##############")
        print("#1."+carne+"                   #")
        print("#2."+carne1+"                  #")
        print("#3.Salir                       #")
        print("################################")
        opc=libreria.validar_menu(input("Ingrese su opcion"))
        if opc==1:
            pollo()
        if opc==2:
            pescado()
import libreria
opc=0
max=3
while opc!=max:
    print("#############MERCADO############")
    print("#1.LACTEOS                     #")
    print("#2.CARNES                      #")
    print("#3.SALIR                       #")
    print("################################")
    opc=libreria.validar_menu(input("Ingrese una opcion"))
    if opc==1:
        lacteos()
    if opc==2:
        carnes()
