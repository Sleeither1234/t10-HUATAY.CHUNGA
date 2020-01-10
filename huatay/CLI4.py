#EJERCICIO 04

def nombres():
    nombres1=libreria.validar_contacto(input("Ingrese su primer nombre "))
    nombres2=libreria.validar_contacto(input("Ingese su segundo nombre "))
    generar_perfil=open("perfil de "+nombres1+".txt","w")
    generar_perfil.write("PERFIL"+"\n"+"primer nombre: "+nombres1+"\n"+"segundo nombre: "+nombres2+"\n")
    generar_perfil.close()
    print("se guardo correctamente")
def Apellidos():
    nombres1 = libreria.validar_contacto(input("Vuelva a ingresar su primer nombre"))
    apellido1=libreria.validar_contacto(input("Ingrese el primer apellido "))
    apellido2=libreria.validar_contacto(input("Ingrese el segundo apellido"))
    generar_perfil = open("perfil de " + nombres1  +".txt", "a")
    generar_perfil.write("\n"+"Primer Apellido: "+apellido1+"\n"+"Segundo Apellido: "+apellido2+"")
    generar_perfil.close()
    print("se guardo correctamente")
def edad():
    nombres1 = libreria.validar_contacto(input("Vuelva a ingresar su primer nombre por favor"))
    edad=libreria.validar_edad(input("Ingrese su edad por favor"))
    generar_perfil = open("perfil de " + nombres1 + ".txt", "a")
    generar_perfil.write("\n"+"Edad: "+edad)
    generar_perfil.close()
    print("se guardo correctamente")
#IMPORTACION DE LA LIBRERIA
import libreria
#ASIGNACION DE LOS RANGOS
opc=0
max=4
#FUNCION MIENTRAS NO CUMPLA LA CAONDICION DE QUE OPCION SEA DIFERENTE DE MAXIMO
while opc!=max:
    print("##########################Perfil######################################################")
    print("#1.Nombres: (para crear su perfil ingrese cada valor desde el 1 hasta el 4 por favor)#")
    print("#2.Apellidos                                                                         #")
    print("#3.Edad                                                                              #")
    print("4.Salir                                                                              #")
    print("######################################################################################")
    #REUTILIZO LA FUNCION ya escrita
    opc=libreria.validar_entero(input("Ingrese su opcion"))
    if opc==1:
        nombres()
    if opc==2:
        Apellidos()
    if opc==3:
        edad()

