def ropa():
    pantalon1="1)PANTALON INDETIX A S/.123 soles"
    camisa1="2)CAMISA INDETIX A S/.98 soles"
    pantalon2="3)PANTALON NIKE A S/145 soles"
    camisa2="4)CAMISA NIKE A S/125 soles"
    pantalon3="5)PANTALON DIOR A S/109 soles"
    camisa3="6)CAMISA DIOR A S/ 78 soles"
    indetix=[pantalon1,camisa1]
    nike=[pantalon2,camisa2]
    dior=[pantalon3,camisa3]
    lista=[indetix,nike,dior]
    print("por favor vrifique la siguinte lista y seleeccione el numero para agregarlo a su archivo de eleccion")
    print(lista)
    nombre=libreria.validar_contacto(input("Ingrese su nombre por favor"))
    eleccion=libreria.validar_eleccion(input("INGRESE EL NUMERO PARA SU ELECCION"))
    if eleccion==1:
        elejir=open("Elecciones del Señor(@) "+nombre+".txt","w")
        elejir.write("se a añadido el producto llamado: "+pantalon1)
        print("se añadido correctamente")
        elejir.close()
    elif eleccion==2:
        elejir = open("Elecciones del Señor(@) " + nombre +".txt", "w")
        elejir.write("se a añadido el producto llamado: " + camisa1)
        print("se añadido correctamente")
        elejir.close()
    elif eleccion==3:
        elejir = open("Elecciones del Señor(@) " + nombre + ".txt", "w")
        elejir.write("se a añadido el producto llamado: " + pantalon2)
        print("se añadido correctamente")
        elejir.close()
    elif eleccion==4:
        elejir = open("Elecciones del Señor(@) " + nombre + ".txt", "w")
        elejir.write("se a añadido el producto llamado: " + camisa2)
        print("se añadido correctamente")
        elejir.close()
    elif eleccion==5:
        elejir = open("Elecciones del Señor(@) " + nombre + ".txt", "w")
        elejir.write("se a añadido el producto llamado: " + pantalon3)
        print("se añadido correctamente")
        elejir.close()
    elif eleccion==6:
        elejir = open("Elecciones del Señor(@) " + nombre + ".txt", "w")
        elejir.write("se a añadido el producto llamado: " + camisa3)
        print("se añadido correctamente")
        elejir.close()
    else:
        print("HA SELECCIONADO UN DIGITO INCORRECTO")
def zapatillas():
    zapatilla1 = "1)ZAPATILLAS INDETIX A S/.123 soles"
    botas1 = "2)BOTAS INDETIX A S/.234 soles"
    zapatilla2 = "3)ZAPATILLAS NIKE A S/345 soles"
    botas2 = "4)BOTAS NIKE A S/325 soles"
    zapatillas3 = "5)ZAPATILLAS  DIOR A S/234 soles"
    botas3= "6)BOTAS  DIOR A S/ 123 soles"
    indetix = [zapatilla1, botas1]
    nike = [zapatilla2, botas2]
    dior = [zapatillas3, botas3]
    lista = [indetix, nike, dior]
    print("por favor vrifique la siguinte lista y seleeccione el numero para agregarlo a su archivo de eleccion")
    print(lista)
    nombre = libreria.validar_contacto(input("Ingrese su nombre por favor"))
    eleccion = libreria.validar_eleccion(input("INGRESE EL NUMERO PARA SU ELECCION"))
    if eleccion == 1:
        elejir = open("Elecciones del Señor(@) " + nombre + ".txt", "w")
        elejir.write("se a añadido el producto llamado: " + zapatilla1)
        print("se añadido correctamente")
        elejir.close()
    elif eleccion == 2:
        elejir = open("Elecciones del Señor(@) " + nombre + ".txt", "w")
        elejir.write("se a añadido el producto llamado: " + botas1)
        print("se añadido correctamente")
        elejir.close()
    elif eleccion == 3:
        elejir = open("Elecciones del Señor(@) " + nombre + ".txt", "w")
        elejir.write("se a añadido el producto llamado: " + zapatilla2)
        print("se añadido correctamente")
        elejir.close()
    elif eleccion == 4:
        elejir = open("Elecciones del Señor(@) " + nombre + ".txt", "w")
        elejir.write("se a añadido el producto llamado: " + botas2)
        print("se añadido correctamente")
        elejir.close()
    elif eleccion == 5:
        elejir = open("Elecciones del Señor(@) " + nombre + ".txt", "w")
        elejir.write("se a añadido el producto llamado: " + zapatillas3)
        print("se añadido correctamente")
        elejir.close()
    elif eleccion == 6:
        elejir = open("Elecciones del Señor(@) " + nombre + ".txt", "w")
        elejir.write("se a añadido el producto llamado: " + botas3)
        print("se añadido correctamente")
        elejir.close()
    else:
        print("HA SELECCIONADO UN DIGITO INCORRECTO")
def accesorios():
    lentes1 = "1)LENTES INDETIX A S/.54 soles"
    gorra1 = "2)GORRA INDETIX A S/.98 soles"
    lentes2 = "3)LENTES NIKE A S/.145 soles"
    gorra2 = "4)GORRA NIKE A S/95 soles"
    lentes3 = "5)LENTES DIOR A S/109 soles"
    gorra3 = "6)GORRA  DIOR A S/ 78 soles"
    indetix = [lentes1, gorra1]
    nike = [lentes2, gorra2]
    dior = [lentes3, gorra3]
    lista = [indetix, nike, dior]
    print("por favor vrifique la siguinte lista y seleeccione el numero para agregarlo a su archivo de eleccion")
    print(lista)
    nombre = libreria.validar_contacto(input("Ingrese su nombre por favor"))
    eleccion = libreria.validar_eleccion(input("INGRESE EL NUMERO PARA SU ELECCION"))
    if eleccion == 1:
        elejir = open("Elecciones del Señor(@) " + nombre + ".txt", "w")
        elejir.write("se a añadido el producto llamado: " + lentes1)
        print("se añadido correctamente")
        elejir.close()
    elif eleccion == 2:
        elejir = open("Elecciones del Señor(@) " + nombre + ".txt", "w")
        elejir.write("se a añadido el producto llamado: " + gorra1)
        print("se añadido correctamente")
        elejir.close()
    elif eleccion == 3:
        elejir = open("Elecciones del Señor(@) " + nombre + ".txt", "w")
        elejir.write("se a añadido el producto llamado: " + lentes2)
        print("se añadido correctamente")
        elejir.close()
    elif eleccion == 4:
        elejir = open("Elecciones del Señor(@) " + nombre + ".txt", "w")
        elejir.write("se a añadido el producto llamado: " + gorra2)
        print("se añadido correctamente")
        elejir.close()
    elif eleccion == 5:
        elejir = open("Elecciones del Señor(@) " + nombre + ".txt", "w")
        elejir.write("se a añadido el producto llamado: " + lentes3)
        print("se añadido correctamente")
        elejir.close()
    elif eleccion == 6:
        elejir = open("Elecciones del Señor(@) " + nombre + ".txt", "w")
        elejir.write("se a añadido el producto llamado: " + gorra3)
        print("se añadido correctamente")
        elejir.close()
    else:
        print("HA SELECCIONADO UN DIGITO INCORRECTO")





import libreria
opc=0
max=4
while opc!=max:
    print("###############TIENDA###############")
    print("#1.ROPA                            #")
    print("#2.Zapatillas                      #")
    print("#3.Accesorios                      #")
    print("#4.Salir                           #")
    print("####################################")
    opc=libreria.validar_entero(input("Ingrese su opcion que desea adquirir "))
    if opc==1:
        ropa()
    if opc==2:
        zapatillas()
    if opc==3:
        accesorios()
