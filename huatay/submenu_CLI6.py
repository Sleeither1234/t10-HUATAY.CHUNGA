def caramelos_goma():
    def masmellow():
        costo=13
        print("Usted ha elejido los masmellow su costo es de "+str(costo))
        archivo=open("golosinas.txt","a")
        archivo.write("Usted ha elejido los masmellow su costo es de "+str(costo))
        print("Datos guardados correctamente")
        archivo.close()
    def gominolas():
        costo = 7.5
        print("Usted ha elejido las gominolas su costo es de " + str(costo))
        archivo = open("golosinas.txt", "a")
        archivo.write("Usted ha elejido los masmellow su costo es de " + str(costo))
        print("Datos guardados correctamente")
        archivo.close()

    opc=0
    max=3
    while opc!=max:
        print("######CARAMELOS DE GOMA ####")
        print("#1.masmellow               #")
        print("#2.gominolas               #")
        print("#3.salir                   #")
        print("############################")
        opc=libreria.validar_menu(input("Ingrese su opcion "))
        if opc==1:
            masmellow()
        if opc==2:
            gominolas()
def caramelos_palo():
    def chupetines():
        costo = 18.50
        print("Usted ha elejido los masmellow su costo es de " + str(costo))
        archivo = open("golosinas.txt", "a")
        archivo.write("Usted ha elejido los masmellow su costo es de " + str(costo))
        print("Datos guardados correctamente")
        archivo.close()

    def paletas():
        costo = 13.45
        print("Usted ha elejido las gominolas su costo es de " + str(costo))
        archivo = open("golosinas.txt", "a")
        archivo.write("Usted ha elejido los masmellow su costo es de " + str(costo))
        print("Datos guardados correctamente")
        archivo.close()

    opc = 0
    max = 3
    while opc!=max:
        print("######CARAMELOS DE PALO ####")
        print("#1.chupetines              #")
        print("#2.paletas                 #")
        print("#3.salir                   #")
        print("############################")
        opc = libreria.validar_menu(input("Ingrese su opcion "))
        if opc == 1:
            chupetines()
        if opc == 2:
            paletas()

import libreria
opc=0
max=3
while opc!=max:
    print("#######GOLOSINAS#######")
    print("#1.CARAMELOS GOMA     #")
    print("#2.CARAMELOS DE PALO  #")
    print("#3.Salir              #")
    print("#######################")
    opc=libreria.validar_menu(input("Ingrese su opcion "))
    if opc==1:
        caramelos_goma()
    if opc==2:
        caramelos_palo()