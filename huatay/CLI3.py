#ejercicio 03

#importacion de la libreria

#realizacion de las funciones en las opciones elejidas
def numero_nacional():
    numero=libreria.validar_telefono(input("Ingrese el numero que desea guardar guardar"))
    nombre=libreria.validar_contacto(input("Ingrese el nombre que usted guste del numero que ingreso"))
    archivo=open(nombre+".txt","w")
    archivo.write("El numero es: "+numero)
    archivo.close()
    print("Se han guardado los datos correctamente")
def numero_internacional():
    archivo=open("numeros.txt","r")
    print(archivo)
    print("Abra el archivo (numeros.txt) por favor ")
    codigo=libreria.validar_codigo(input("INGRESE EL CODIGO DEL  PAIS ANTES DE PONER EL NUMERO PORFAVOR"))
    print(codigo)
    archivo.close()
    numero = libreria.validar_contacto_internacional(input("Ingrese el numero que desea guardar guardar"))
    nombre = libreria.validar_contacto(input("Ingrese el nombre que usted guste del numero que ingreso"))
    archivo = open(nombre + ".txt", "w")
    archivo.write("El numero es: " + codigo+numero)
    archivo.close()
    print("Se han guardado los datos correctamente")
#asignacion de la opcion minima y max
opc=0
max=3
import libreria

#se iingresa la funcion mientras
while opc!=max:
    #se imprime el menu
    print("################################CONTACTOS#############################")
    print("#1.GUARDAR CONTACTO (Si es nacional el numero seleccione esta opcion)#")
    print("#2.GUARDAR CONTACTO INTERNACIONAL                                    #")
    print("#3.SALIR                                                             #")
    print("######################################################################")
    opc=libreria.validar_menu(input("Ingrese su opcion: "))
    #condicionales a partir de la condicion dada
    if opc==1:
        numero_nacional()
    if opc==2:
        numero_internacional()