#ejercicio 01

#importacion de la libreria
import libreria

#funciones segun la opcion elejida
def platos():
    archivo=open("CLI1.txt") #se abre un archivo
    platos=archivo.readline(    )#se nombra la variable platos a la primera linea del archivo txt
    print(platos)           #se imprime la variable platos
    archivo.close()         #se cierra el archivo obligatorio
    a="ARROZ CON PATO"
    b="CABRITO"
    c="CHACHO MECHADO"   #asignacion de variables
    d="LOMO SALTADO"
    lista=[a,b,c,d]    #creacion de una lista
    #ingresar datos a laa variable para elejir una letra nos devolvera una variable de la lista
    elejir=input("ingrese la letra elejida para seleccionar su plato")
    #condicion multiple si es incorrecta nos devolvera al menu
    if elejir.upper()=="A":
        print("USTED A ELEJIDO "+ a)
    elif elejir.upper()=="B":
        print("Usted a elejido "+b)
    elif elejir.upper()=="C":
         print("Usted a elejido "+c)
    elif elejir.upper()=="D":
          print("Usted a elejido "+d)
    else:
        print("letra equivocada,volviendo al menu de inicio")


def bebidas():
    archivo=open("CLI1.txt") #se abre un archivo txt
    bebidas=archivo.readline()  #se nombra la variable bebidas y comienza desde la primera linea del archivo txt
    bebidas=archivo.readline() #se avanza otra linea  en donde se empezara a leer el archivo txt
    print(bebidas)             #se imprime la segunda linea del txt
    archivo.close()             #se cierra el archivo obligatorio
    a = "CHICHA MORADA"
    b = "LIMA"
    c = "MARACUYA"
    d = "LIMONADA"        #"bis"
    e="CEBADA"
    lista = [a, b, c, d,e]
    elejir = input("ingrese la letra elejida para seleccionar su bebida")
    if elejir.upper() == "A":
        print("USTED A ELEJIDO " + a)
    elif elejir.upper() == "B":
        print("Usted a elejido " + b)
    elif elejir.upper() == "C":           #bis
        print("Usted a elejido " + c)
    elif elejir.upper() == "D":
        print("Usted a elejido " + d)
    elif elejir.upper()=="E":
        print("Usted a elejido "+e)
    else:
        print("letra equivocada,volviendo al menu de inicio")
def postres():
    archivo=open("CLI1.txt")   #se abre un archivo txt
    postres=archivo.readline() #se nombra la variable postres en donde abrimos la primera linea del txt
    postres=archivo.readline() #se avanza una linea del archivo txt
    postres = archivo.readline() #se avanza otra linea del archivo txt
    print(postres)             #se presenta la tercera linea del archivo txt
    archivo.close()            #se cierra el archivo obligatorio
    a = "GELATINA"           #asignacion de variables
    b = "FLAN"
    c = "ARROZ CON LECHE"
    d = "MAZAMORRA"
    lista = [a, b, c, d] #se crea una lista a partir de la variables creadas
    #se pide datos para seleccionar lo pedido en la lista
    elejir = input("ingrese la letra elejida para seleccionar su postre")
     #funcion condicional multiple segun sea la letra elejida se imprimira la variable
    if elejir.upper() == "A":
        print("USTED A ELEJIDO " + a)
    elif elejir.upper() == "B":
        print("Usted a elejido " + b)
    elif elejir.upper() == "C":
        print("Usted a elejido " + c)
    elif elejir.upper() == "D":
        print("Usted a elejido " + d)
    else:
        print("letra equivocada,volviendo al menu de inicio")

# se nombra las variables que serian el min y el max
opc=0
max=4
while opc!=max: #se asigna la funcion  ( mientras no cumpla la condicion de que opc sea diferente de 4 el bucle no terminara)
    #se hace una impresion del menu
    print("##################MENU###########################")
    print("#1.PLATOS A LA CARTA  (seleccione 1 para ver)   #")
    print("#2.BEBIDAS  (seleccione 2 para ver)             #")
    print("#3.POSTRES  (seleccione 3 para ver)             #")
    print("#4.SALIR                                        #")
    print("#################################################")


    opc=libreria.validar_entero(input("ingrese un valor")) #se asigna el valor opcion el cuall sera validado desde la libreria
    if opc==1: #si la opcion elejida es 1 pasa ala funcion platos()
        platos()
    if opc==2: #si la opcion elejida es 2 pasa a la funcion bebidas()
        bebidas()
    if opc==3: #si la opcion elejida es 3 pasa a la funcion postres()
        postres()

