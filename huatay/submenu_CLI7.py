def f_constante():
    def ver_grafica():
        print("##########################")
        print("#      | F.constante     #")
        print("#   ___|________         #")
        print("#______|_______          #")
        print("#      |                 #")
        print("##########################")
    def forma():
        print("SU forma es: Y=b")
        guardar=input(input("DESEA GENERAR UNA FUNCION CON ESTA FORMA? SI(1) O NO(0)"))
        if guardar==1:
            b=libreria.validar_suma(input("Ingrese el valor de b"))
            print("FUNCION generada con forma y="+str(b))
            archivo=open("funciones.txt","w")
            archivo.write("FUNCION generada con forma y="+str(b))
            print("se guardaron los datos automaticamente")
            archivo.close()
    opc=0
    max=3
    while opc!=max:

        print("########F.CONSTANTE#######")
        print("#1.VER grafica           #")
        print("#2.FORMA                 #")
        print("#3.salir                 #")
        print("##########################")
        opc=libreria.validar_menu(input("Ingrese su opcion"))
        if opc==1:
            ver_grafica()
        if opc==2:
            forma()
def f_recta():
    def ver_grafica():
        print("##########################")
        print("#F.recta   |  /          #")
        print("#          | /           #")
        print("#      ____|/_______     #")
        print("#          /             #")
        print("##########################")
    def forma():
        print("SU forma es: Y=ax+b")
        guardar=input(input("DESEA GENERAR UNA FUNCION CON ESTA FORMA? SI(1) O NO(0)"))
        if guardar==1:
            a=libreria.validar_suma(input("Ingrese el valor de a"))
            b=libreria.validar_suma(input("Ingrese el valor de b"))
            print("FUNCION generada con forma y="+str(a)+"x"+"+"+str(b))
            archivo=open("funciones.txt","w")
            archivo.write("FUNCION generada con forma y="+str(a)+"x"+"+"+str(b))
            print("se guardaron los datos automaticamente")
            archivo.close()
    opc=0
    max=3
    while opc!=max:
        print("########F.RECTA###########")
        print("#1.VER grafica           #")
        print("#2.FORMA                 #")
        print("#3.salir                 #")
        print("##########################")
        opc=libreria.validar_menu(input("Ingrese su opcion"))
        if opc==1:
            ver_grafica()
        if opc==2:
            forma()


import libreria
opc=0
max=3
while opc!=max:
    print("#########Funciones#####")
    print("#1.Funcion constante  #")
    print("#2.Funcion recta      #")
    print("#3.Salir              #")
    print("#######################")
    opc=libreria.validar_menu(input("Ingrese su opcion "))
    if opc==1:
        f_constante()
    if opc==2:
        f_recta()