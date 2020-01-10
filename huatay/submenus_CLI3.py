def potenciacion():
    def poten_cuadrado():
        numero=libreria.validar_suma(input("Ingrese el numero que desea elevar"))
        elevacion=numero**2
        print("El resultado de la elevacion al cudadrado del numero "+str(numero)+" es: "+str(elevacion))
        guardar=libreria.validar_suma(input("Deseas guardar el resultado en un archivo txt? SI(1)O NO(0)"))
        if guardar==1:
            archivo=open("potenciacion_cuadrado.txt","w")
            archivo.write("El resultado de la elevacion al cudadrado del numero "+str(numero)+" es: "+str(elevacion))
            print("se han guardado correctamente los datos")
            archivo.close()
        elif guardar==0:
            print("Ok no se guardara ningun dato")
        else:
            print("H ingresado un comando invalido")
    def poten_enesimo():
        numero = libreria.validar_suma(input("Ingrese el numero que desea elevar"))
        enesimo=libreria.validar_suma(input("Ingre el termino a que desea elevar"))
        elevacion = numero **enesimo
        print("El resultado de la elevacion al "+str(enesimo)+" del numero " + str(numero) + " es: " + str(elevacion))
        guardar = libreria.validar_suma(input("Deseas guardar el resultado en un archivo txt? SI(1)O NO(0)"))
        if guardar == 1:
            archivo = open("potenciacion_enesimo.txt", "w")
            archivo.write("El resultado de la elevacion al cudadrado del numero " + str(numero) + " es: " + str(elevacion))
            print("se han guardado correctamente los datos")
            archivo.close()
        elif guardar == 0:
            print("Ok no se guardara ningun dato")
        else:
            print("H ingresado un comando invalido")
    opc=0
    max=3
    while opc!=3:

        print("#######POTENCIACION############################")
        print("#1.POTENCIACION AL CUADRADO DE UN NUMERO      #")
        print("#2.POTENCIACION ELEVADO A UN ENESIMO TERMINO  #")
        print("#3.Salir                                      #")
        print("###############################################")
        opc=libreria.validar_menu(input("Ingrese su opcion"))
        if opc==1:
            poten_cuadrado()
        if opc==2:
            poten_enesimo()
def radicacion():
    import math
    def radi_cuadrado():
        numero=libreria.validar_suma(input("Ingrese su numero"))
        resultado=math.sqrt(numero)
        print("el resultado de la radicaion del numero "+str(numero)+" es: "+str(resultado))
        guardar=libreria.validar_suma(input("DESEA GUARDAR LOS DATOS? SI(1) O NO(0)"))
        if guardar==1:
            archivo=open("radi_cuadrado.txt","w")
            archivo.write(print("el resultado de la radicaion del numero "+str(numero)+" es: "+str(resultado)))
            print("Se ha guardado correctamente ")
            archivo.close()
        elif guardar==0:
            print("ok no se guardara ningun dato")
        else:
            print("Comando invalido")
    def radi_decimal():
        numero = libreria.validar_float(input("Ingrese su numero"))
        resultado = math.sqrt(numero)
        print("el resultado de la radicaion del numero " + str(numero) + " es: " + str(resultado))
        guardar = libreria.validar_suma(input("DESEA GUARDAR LOS DATOS? SI(1) O NO(0)"))
        if guardar == 1:
            archivo = open("radi_cuadrado.txt", "w")
            archivo.write(print("el resultado de la radicaion del numero " + str(numero) + " es: " + str(resultado)))
            print("Se ha guardado correctamente ")
            archivo.close()
        elif guardar == 0:
            print("ok no se guardara ningun dato")
        else:
            print("Comando invalido")

    opc=0
    max=3
    while opc!=max:
        print("###################radicacion############")
        print("#1.Radicacion al cuadrado               #")
        print("#2.Radicacion al cuadrado con decimales #")
        print("#3.Salir                                #")
        print("#########################################")
        opc=libreria.validar_menu(input("ingrese su opcion"))
        if opc==1:
            radi_cuadrado()
        if opc==2:
            radi_decimal()
import libreria
opc=0
max=3
while opc!=max:
    print("#######################")
    print("#1.POTENCIACION       #")
    print("#2.Radicacion         #")
    print("#3.Salir              #")
    print("#######################")
    opc=libreria.validar_menu(input("Ingrese su opcion "))
    if opc==1:
        potenciacion()
    if opc==2:
        radicacion()