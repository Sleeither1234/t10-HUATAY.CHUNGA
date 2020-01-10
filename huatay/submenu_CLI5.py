def monkey():
    def iniciar_juego():
        print("BIENVENIDO A MONKEY")
        nombre=libreria.validar_apellido(input("INGRESE SU NOMBRE"))
        archivo=open(nombre+".txt","w")
        puntos=libreria.validar_suma(input("Inrese su score"))
        archivo.write("JUGADOR: "+nombre+"\n"+"PUNTOS: "+str(puntos))
        print("Guardando datos")
        archivo.close()

    def  guardar_juego():
        guardar_juego=int(input("DESEA CONTINUAR LA PARTIDA? SI(1) O NO(0)"))
        if guardar_juego==1:
            print("continuando juego")
            nombre = libreria.validar_apellido(input("INGRESE SU NOMBRE"))
            archivo = open(nombre + ".txt", "a")
            puntos = libreria.validar_suma(input("Inrese su score"))
            archivo.write("JUGADOR: " + nombre + "\n" + "PUNTOS: " + str(puntos))
            print("Guardando datos")
            archivo.close()

        elif guardar_juego==0:
            print("ok comenzando nueva partida")
            iniciar_juego()

        else:
            print("COMANDO INVALIDO")

    opc=0
    max=3
    while opc!=max:

        print("###########MONKEY########")
        print("#1.INICIAR JUEGO        #")
        print("#2.Guardar score        #")
        print("#3.Salir                #")
        print("#########################")
        opc=libreria.validar_menu(input("Ingrese su opcion"))
        if opc==1:
            iniciar_juego()
        if opc==2:
            guardar_juego()
def mario():
    def iniciar_juego():
        print("BIENVENIDO A MARIO BROSS")
        nombre = libreria.validar_apellido(input("INGRESE SU NOMBRE"))
        archivo = open(nombre + ".txt", "w")
        puntos = libreria.validar_suma(input("Inrese su score"))
        archivo.write("JUGADOR: " + nombre + "\n" + "PUNTOS: " + str(puntos))
        print("Guardando datos")
        archivo.close()

    def guardar_juego():
        guardar_juego = int(input("DESEA CONTINUAR LA PARTIDA? SI(1) O NO(0)"))
        if guardar_juego == 1:
            print("continuando juego")
            nombre = libreria.validar_apellido(input("INGRESE SU NOMBRE"))
            archivo = open(nombre + ".txt", "a")
            puntos = libreria.validar_suma(input("Inrese su score"))
            archivo.write("JUGADOR: " + nombre + "\n" + "PUNTOS: " + str(puntos))
            print("Guardando datos")
            archivo.close()

        elif guardar_juego == 0:
            print("ok comenzando nueva partida")
            iniciar_juego()

        else:
            print("COMANDO INVALIDO")

    opc = 0
    max = 3
    while opc!=max:
        print("#########MARIO BROSS#####")
        print("#1.INICIAR JUEGO        #")
        print("#2.Guardar score        #")
        print("#3.Salir                #")
        print("#########################")
        opc = libreria.validar_menu(input("Ingrese su opcion"))
        if opc == 1:
            iniciar_juego()
        if opc == 2:
            guardar_juego()

import libreria
opc=0
max=3
while opc!=max:
    print("########ARCADE###############")
    print("#1.MONKEY KING              #")
    print("#2.MARIO BROSS              #")
    print("#3.Salir                    #")
    print("#############################")
    opc=libreria.validar_menu(input("Ingrese su opcion "))
    if opc==1:
        monkey()
    if opc==2:
        mario()
