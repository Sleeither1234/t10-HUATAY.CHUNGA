def rifles():
    def carabina():
        a="1)CARABINA M1"
        b="2)CARABINA M4"
        lista=[a,b]
        comprar=int(input("Desea comprar las siguientes armas? SI(1)O NO(0)"))
        if comprar==1:
            print(lista)
            print("Estas son las siguientes armas disponibles")
            guardar=libreria.validar_suma(input("SELECCIONE SU OPCION"))
            if guardar==1:
                archivo=open("compras.txt","w")
                archivo.write("Se ha añadido a "+a+" correctamente")
                print("Añadiendo al carrito")
                archivo.close()
            if guardar==2:
                archivo = open("compras.txt", "w")
                archivo.write("Se ha añadido a " + b + " correctamente")
                print("Añadiendo al carrito")
                archivo.close()
            else:
                print("Comando invalido")
        if comprar==0:
            print("ok no se añadira al carrito")
        else:
            print("Comando invalido")
    def paint_ball():
        a = "1)PAINT BALL M17"
        b = "2)PAINT BALL T5"
        lista = [a, b]
        comprar = int(input("Desea comprar las siguientes armas? SI(1)O NO(0)"))
        if comprar == 1:
            print(lista)
            print("Estas son las siguientes armas disponibles")
            guardar = libreria.validar_suma(input("SELECCIONE SU OPCION"))
            if guardar == 1:
                archivo = open("compras.txt", "w")
                archivo.write("Se ha añadido a " + a + " correctamente")
                print("Añadiendo al carrito")
                archivo.close()
            if guardar == 2:
                archivo = open("compras.txt", "w")
                archivo.write("Se ha añadido a " + b + " correctamente")
                print("Añadiendo al carrito")
                archivo.close()
            else:
                print("Comando invalido")
        if comprar == 0:
            print("ok no se añadira al carrito")
        else:
            print("Comando invalido")
    opc=0
    max=3
    while opc!=max:
        print("########R#########")
        print("#1.CARABINA      #")
        print("#2.PAINT BALL    #")
        print("#3.salir         #")
        print("##################")
        opc=libreria.validar_menu(input("Ingrese su opcion"))
        if opc==1:
            carabina()
        if opc==2:
            paint_ball()
def sniper():
    def single():
        a="1)SINGLE BUN"
        b="2)SINGLE PANAMA BOSS"
        lista=[a,b]
        comprar=int(input("Desea comprar las siguientes armas? SI(1)O NO(0)"))
        if comprar==1:
            print(lista)
            print("Estas son las siguientes armas disponibles")
            guardar=libreria.validar_suma(input("SELECCIONE SU OPCION"))
            if guardar==1:
                archivo=open("compras.txt","w")
                archivo.write("Se ha añadido a "+a+" correctamente")
                print("Añadiendo al carrito")
                archivo.close()
            if guardar==2:
                archivo = open("compras.txt", "w")
                archivo.write("Se ha añadido a " + b + " correctamente")
                print("Añadiendo al carrito")
                archivo.close()
            else:
                print("Comando invalido")
        if comprar==0:
            print("ok no se añadira al carrito")
        else:
            print("Comando invalido")
    def automatica():
        a = "1)AUTOMATIC MK14"
        b = "2)AUTOMATIC SWD"
        lista = [a, b]
        comprar = int(input("Desea comprar las siguientes armas? SI(1)O NO(0)"))
        if comprar == 1:
            print(lista)
            print("Estas son las siguientes armas disponibles")
            guardar = libreria.validar_suma(input("SELECCIONE SU OPCION"))
            if guardar == 1:
                archivo = open("compras.txt", "w")
                archivo.write("Se ha añadido a " + a + " correctamente")
                print("Añadiendo al carrito")
                archivo.close()
            if guardar == 2:
                archivo = open("compras.txt", "w")
                archivo.write("Se ha añadido a " + b + " correctamente")
                print("Añadiendo al carrito")
                archivo.close()
            else:
                print("Comando invalido")
        if comprar == 0:
            print("ok no se añadira al carrito")
        else:
            print("Comando invalido")
    opc=0
    max=3
    while opc!=max:
        print("####SNIPER########")
        print("#1.SINGLE        #")
        print("#2.AUTOMATICA    #")
        print("#3.salir         #")
        print("##################")
        opc=libreria.validar_menu(input("Ingrese su opcion"))
        if opc==1:
            single()
        if opc==2:
            automatica()
import libreria
opc=0
max=3
while opc!=max:
    print("########ARMAS##########")
    print("#1.RIFLES             #")
    print("#2.SNIPER             #")
    print("#3.Salir              #")
    print("#######################")
    opc=libreria.validar_menu(input("Ingrese su opcion "))
    if opc==1:
        rifles()

    if opc==2:
        sniper()