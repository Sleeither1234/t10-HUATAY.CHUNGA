
def rock_80():
    can1="1)Rick Astley - Never Gonna Give You Up"
    can2="2)Europe - The Final Countdown "
    can3="3)Cyndi Lauper - Girls Just Want To Have Fun"
    can4="4)Guns N' Roses - November Rain"
    can5="5)a-ha - Take On Me"
    lista=[can1,can2,can3,can4,can5]
    print(lista)
    importante=libreria.validar_dns(input("Ingrese su valor"))
    if importante==1:
        print("reproduciendo: "+can1)
        guardar=int(input("Desea guardarlo en su lista de favoritos SI(1) O NO(0)?"))
        if guardar==1:
            archivo=open("favoritos.txt","a")
            archivo.write("nombre: "+can1)
            print("se ha guardado correctamente")
            archivo.close()
        elif guardar==0:
            print("OK NO SE GUARDARA NINGUN DATO")
        else:
            print("Comando invalido")
    elif importante==2:
        print("reproduciendo: " + can2)
        guardar = int(input("Desea guardarlo en su lista de favoritos SI(1) O NO(0)?"))
        if guardar == 1:
            archivo = open("favoritos.txt", "a")
            archivo.write("nombre: " + can2)
            print("se ha guardado correctamente")
            archivo.close()
        elif guardar == 0:
            print("OK NO SE GUARDARA NINGUN DATO")
        else:
            print("Comando invalido")
    elif importante==3:
        print("reproduciendo: " + can3)
        guardar = int(input("Desea guardarlo en su lista de favoritos SI(1) O NO(0)?"))
        if guardar == 1:
            archivo = open("favoritos.txt", "a")
            archivo.write("nombre: " + can3)
            print("se ha guardado correctamente")
            archivo.close()
        elif guardar == 0:
            print("OK NO SE GUARDARA NINGUN DATO")
        else:
            print("Comando invalido")
    elif importante==4:
        print("reproduciendo: " + can4)
        guardar = int(input("Desea guardarlo en su lista de favoritos SI(1) O NO(0)?"))
        if guardar == 1:
            archivo = open("favoritos.txt", "a")
            archivo.write("nombre: " + can4)
            print("se ha guardado correctamente")
            archivo.close()
        elif guardar == 0:
            print("OK NO SE GUARDARA NINGUN DATO")
        else:
            print("Comando invalido")
    elif importante==5:
        print("reproduciendo: " + can5)
        guardar = int(input("Desea guardarlo en su lista de favoritos SI(1) O NO(0)?"))
        if guardar == 1:
            archivo = open("favoritos.txt", "a")
            archivo.write("nombre: " + can5)
            print("se ha guardado correctamente")
            archivo.close()
        elif guardar == 0:
            print("OK NO SE GUARDARA NINGUN DATO")
        else:
            print("Comando invalido")
    else:
        print("HA INGRESADO UN NUMERO INVALIDO")
def pop_80():
    can1 = "1)Another One Bites the Dust-Queen"
    can2 = "2)Tunnel of Love-Dire Straits"
    can3 = "3)Celebration-Kool & The Gang"
    can4 ="4)Funky Town-Lipps !nc"
    can5 ="5)Vienna-Ultravox"
    lista = [can1, can2, can3, can4, can5]
    print(lista)
    importante = libreria.validar_dns(input("Ingrese su valor"))
    if importante == 1:
        print("reproduciendo: " + can1)
        guardar = int(input("Desea guardarlo en su lista de favoritos SI(1) O NO(0)?"))
        if guardar == 1:
            archivo = open("favoritos.txt", "a")
            archivo.write("nombre: " + can1)
            print("se ha guardado correctamente")
            archivo.close()
        elif guardar == 0:
            print("OK NO SE GUARDARA NINGUN DATO")
        else:
            print("Comando invalido")
    elif importante == 2:
        print("reproduciendo: " + can2)
        guardar = int(input("Desea guardarlo en su lista de favoritos SI(1) O NO(0)?"))
        if guardar == 1:
            archivo = open("favoritos.txt", "a")
            archivo.write("nombre: " + can2)
            print("se ha guardado correctamente")
            archivo.close()
        elif guardar == 0:
            print("OK NO SE GUARDARA NINGUN DATO")
        else:
            print("Comando invalido")
    elif importante == 3:
        print("reproduciendo: " + can3)
        guardar = int(input("Desea guardarlo en su lista de favoritos SI(1) O NO(0)?"))
        if guardar == 1:
            archivo = open("favoritos.txt", "a")
            archivo.write("nombre: " + can3)
            print("se ha guardado correctamente")
            archivo.close()
        elif guardar == 0:
            print("OK NO SE GUARDARA NINGUN DATO")
        else:
            print("Comando invalido")
    elif importante == 4:
        print("reproduciendo: " + can4)
        guardar = int(input("Desea guardarlo en su lista de favoritos SI(1) O NO(0)?"))
        if guardar == 1:
            archivo = open("favoritos.txt", "a")
            archivo.write("nombre: " + can4)
            print("se ha guardado correctamente")
            archivo.close()
        elif guardar == 0:
            print("OK NO SE GUARDARA NINGUN DATO")
        else:
            print("Comando invalido")
    elif importante == 5:
        print("reproduciendo: " + can5)
        guardar = int(input("Desea guardarlo en su lista de favoritos SI(1) O NO(0)?"))
        if guardar == 1:
            archivo = open("favoritos.txt", "a")
            archivo.write("nombre: " + can5)
            print("se ha guardado correctamente")
            archivo.close()
        elif guardar == 0:
            print("OK NO SE GUARDARA NINGUN DATO")
        else:
            print("Comando invalido")
    else:
        print("HA INGRESADO UN NUMERO INVALIDO")


import libreria
opc=0
max=3
while opc!=max:
    print("######################CANCIONES DE LOS 80############")
    print("#1.ROCK DE LOS 80 MAS FAMOSOS                       #")
    print("#2.POP DE LOS 80  MAS FAMOSOS                       #")
    print("#3.SALIR                                            #")
    print("#####################################################")
    opc=libreria.validar_menu(input("INGRESE SU OPCION"))

    if opc==1:
        rock_80()
    if opc==2:
        pop_80()
