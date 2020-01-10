def aves():
    def pelicano():
        print("Usted a elejido PELICANO ")
        guardar=int(input("desea guardarlo como su ave favorito? SI(1)O NO(0)"))
        if guardar==1:
            archivo=open("animales.txt","w")
            archivo.write("Su ave de alta mar favorito es el PELICANO")
            archivo.close()
        if guardar==0:
            print("Ok NO SE GUARDARA NINGUN DATO")
        else:
            print("Comando invalido")
    def gallo():
        print("Usted a elejido gallo ")
        guardar = int(input("desea guardarlo como su ave favorito? SI(1)O NO(0)"))
        if guardar == 1:
            archivo = open("animales.txt", "w")
            archivo.write("Su ave de corral favorito es el GALLO")
            archivo.close()
        if guardar == 0:
            print("Ok NO SE GUARDARA NINGUN DATO")
        else:
            print("Comando invalido")
    def loro():
        print("Usted a elejido  LORO ")
        guardar=int(input("desea guardarlo como su ave favorito? SI(1)O NO(0)"))
        if guardar==1:
            archivo=open("animales.txt","w")
            archivo.write("Su ave silvestre favorito es el LORO")
            archivo.close()
        if guardar==0:
            print("Ok NO SE GUARDARA NINGUN DATO")
        else:
            print("Comando invalido")
    opc = 0
    max = 3
    while opc != 3:
        print("#########AVES############")
        print("#1.PELICANO             #")
        print("#2.GALLO                #")
        print("#3.PERRO                #")
        print("#4.salir                #")
        print("#########################")
        opc = libreria.validar_entero(input("Ingrese su opcion"))
        if opc == 1:
            pelicano()
        if opc == 2:
            gallo()
        if opc == 3:
            loro()

def mamiferos():
    def leon():
        print("Usted a elejido leon ")
        guardar=int(input("desea guardarlo como su animal favorito? SI(1)O NO(0)"))
        if guardar==1:
            archivo=open("animales.txt","w")
            archivo.write("Su animal salvaje favorito es el LEON")
            archivo.close()
        if guardar==0:
            print("Ok NO SE GUARDARA NINGUN DATO")
        else:
            print("Comando invalido")
    def cerdo():
        print("Usted a elejido cerdo ")
        guardar = int(input("desea guardarlo como su animal favorito? SI(1)O NO(0)"))
        if guardar == 1:
            archivo = open("animales.txt", "w")
            archivo.write("Su animal de corral favorito es el CERDO")
            archivo.close()
        if guardar == 0:
            print("Ok NO SE GUARDARA NINGUN DATO")
        else:
            print("Comando invalido")
    def perro():
        print("Usted a elejido  PERRO ")
        guardar=int(input("desea guardarlo como su animal favorito? SI(1)O NO(0)"))
        if guardar==1:
            archivo=open("animales.txt","w")
            archivo.write("Su animal domestico favorito es el LEON")
            archivo.close()
        if guardar==0:
            print("Ok NO SE GUARDARA NINGUN DATO")
        else:
            print("Comando invalido")
    opc = 0
    max = 3
    while opc != 3:
        print("#########MAMIFEROS#######")
        print("#1.LEON                 #")
        print("#2.CERDO                #")
        print("#3.PERRO                #")
        print("#4.salir                #")
        print("#########################")
        opc = libreria.validar_entero(input("Ingrese su opcion"))
        if opc == 1:
            leon()
        if opc == 2:
            cerdo()
        if opc == 3:
            perro()


import libreria
opc=0
max=3
while opc!=max:
    print("#######ESPECIES########")
    print("#1.AVES               #")
    print("#2.MAMIFEROS          #")
    print("#3.Salir              #")
    print("#######################")
    opc=libreria.validar_menu(input("Ingrese su opcion "))
    if opc==1:
        aves()
    if opc==2:
        mamiferos()