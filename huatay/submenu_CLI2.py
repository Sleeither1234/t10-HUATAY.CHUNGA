def suma():
    def sumar_2_numeros():
        primer=libreria.validar_suma(input("Ingrese el primer valor"))
        segundo=libreria.validar_suma(input("Ingrese el segundo valor"))
        suma=(primer)+(segundo)
        print("La suma de "+str(primer)+" y "+str(segundo)+" es: "+str(suma))
        guardar=input("DESEA GUARDAR LOS DATOS? SI(1)O NO(0)")
        if guardar==1:
            archivo=open("suma2.txt","w")
            archivo.write("La suma de "+str(primer)+" y "+str(segundo)+" es: "+str(suma))
            print("DATOS GUARDADOS CORRECTAMENTE")
            archivo.close()

        elif guardar==0:
            print("OK NO SE GUARDARA EL DATO")
        else:
            print("Ha ingresado un comando invalido")
    def sumar_3_numeros():
        primer = libreria.validar_suma(input("Ingrese el primer valor"))
        segundo = libreria.validar_suma(input("Ingrese el segundo valor"))
        tercero=libreria.validar_suma(input("Ingrese el tercer valor"))
        suma = primer + segundo+tercero
        print("La suma de " + str(primer) + "," + str(segundo)+ "y "+ str(tercero)+" es: " + str(suma))
        guardar = input("DESEA GUARDAR LOS DATOS? SI(1)O NO(0)")
        if guardar == 1:
            archivo = open("suma3.txt", "w")
            archivo.write("La suma de " + str(primer) + "," + str(segundo) + "y " + str(tercero) + " es: " + str(suma))
            print("DATOS GUARDADOS CORRECTAMENTE")
            archivo.close()

        elif guardar == 0:
            print("OK NO SE GUARDARA EL DATO")
        else:
            print("Ha ingresado un comando invalido")
    opc=0
    max=3
    while opc!=max:
        print("######Suma#################")
        print("#1.Sumar dos numeros      #")
        print("#2.Sumar tres numeros     #")
        print("#3.Salir                  #")
        print("###########################")
        opc=libreria.validar_menu(input("Ingrese su opcion "))
        if opc==1:
            sumar_2_numeros()
        if opc==2:
            sumar_3_numeros()
def resta():
    def restar_2_numeros():
        primer = libreria.validar_suma(input("Ingrese el primer valor"))
        segundo = libreria.validar_suma(input("Ingrese el segundo valor"))
        resta = primer - segundo
        print("La resta de " + str(primer) + " y " + str(segundo) + " es: " + str(resta))
        guardar = input("DESEA GUARDAR LOS DATOS? SI(1)O NO(0)")
        if guardar == 1:
            archivo = open("resta2.txt", "w")
            archivo.write("La resta de " + str(primer) + " y " + str(segundo) + " es: " + str(resta))
            print("DATOS GUARDADOS CORRECTAMENTE")
            archivo.close()

        elif guardar == 0:
            print("OK NO SE GUARDARA EL DATO")
        else:
            print("Ha ingresado un comando invalido")

    def restar_3_numeros():
        primer = libreria.validar_suma(input("Ingrese el primer valor"))
        segundo = libreria.validar_suma(input("Ingrese el segundo valor"))
        tercero = libreria.validar_suma(input("Ingrese el tercer valor"))
        resta = primer - segundo - tercero
        print("La resta de " + str(primer) + "," + str(segundo) + "y " + str(tercero) + " es: " + str(resta))
        guardar = input("DESEA GUARDAR LOS DATOS? SI(1)O NO(0)")
        if guardar == 1:
            archivo = open("resta3.txt", "w")
            archivo.write("La resta de " + str(primer) + "," + str(segundo) + "y " + str(tercero) + " es: " + str(resta))
            print("DATOS GUARDADOS CORRECTAMENTE")
            archivo.close()

        elif guardar == 0:
            print("OK NO SE GUARDARA EL DATO")
        else:
            print("Ha ingresado un comando invalido")

    opc = 0
    max = 3
    while opc!=max:

        print("######Suma#################")
        print("#1.Restar dos numeros     #")
        print("#2.Restar tres numeros    #")
        print("#3.Salir                  #")
        print("###########################")
        opc = libreria.validar_menu(input("Ingrese su opcion "))
        if opc == 1:
            restar_2_numeros()
        if opc == 2:
            restar_3_numeros()


import libreria
opc=0
max=3
while opc!=max:
    print("#####CALCULADORA######")
    print("#1.SUMA              #")
    print("#2.RESTA             #")
    print("#3.SALIR             #")
    print("######################")
    opc=libreria.validar_menu(input("Ingrese su opcion "))
    if opc==1:
        suma()
    if opc==2:
        resta()
