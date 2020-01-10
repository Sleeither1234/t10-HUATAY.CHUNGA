#ejercicio 02
# se muestra las funciones dependiendo la opcion elejida
def suma():
    #asignacion de valores dentro de la funcion
    primer_numero=libreria.validar_numero(input("Ingrese el primer valor "))
    segundo_numero=libreria.validar_numero(input("Ingrese el segundo valor"))
    #realizacion del calculo de los valores dados
    suma=(int(primer_numero)+int(segundo_numero))
    #se imprimer un mensaje con el resultado y se pregunta al usuario si desea guardar los datos
    print("La suma de los valores dados es : "+str(suma))
    print("Desea guardar este dato?")
    valor=int(input("SI(1) o NO(0)"))
    #condicional multiple
    if valor==1:
            #SE ABRE UN ARCHIVO , SE GUARDA EL DATO , SE IMPRIME UN MENSAJE EN EL CUAL SE GUARDA LOS DATOS Y SE CIERRA EL ARCHIVO
            archivo=open("CLI2.txt","a")
            archivo.write("el valor de la suma de los numeros "+primer_numero+" y "+segundo_numero+"es :"+str(suma))
            print("se han guardado los datos correctamente")
            archivo.close()
    #SI EL VALOR ES IGUAL A 0 ENTONCES NO SE GUARDARA NINGUN DATO
    elif valor==0:
        print("OK, no se guardara nigun dato")
    #SI EL VALOR ES DIFERENTE APARECERA UN MENSAJE QUE EL VALOR ES FALSA Y LO REGRESARA AL MENU
    else:
        print("EL VALOR INGRESADO ES FALSO")

#Y asi con las demas funciones tienen la misma estructura
def resta():
    primer_valor=libreria.validar_numero(input("Ingrese el primer valor: "))
    segundo_valor=libreria.validar_numero(input("Ingrese el segundo valor"))
    resta=int(primer_valor)-int(segundo_valor)
    print("La resta de los valores dados es: "+str(resta))
    print("Desea guardar el resultado de la resta?")
    valor=int(input("SI(1) O NO(0)"))
    if valor==1:
        archivo=open("CLI2.txt","a")
        archivo.write("El valor de la resta de los valores "+primer_valor+" y "+segundo_valor+" es: "+str(resta))
        print("se han guardado los datos correctamente")
        archivo.close()
    elif valor==0:
        print("OK no se guardaran los datos")
    else:
        print("EL NUMERO INGRESADO ES FALSO")
def multiplicacion():
    digit1=libreria.validar_numero(input("Ingrese el primer valor: "))
    digit2=libreria.validar_numero(input("Irgrese el segundo valor: "))
    multiplicacion=int(digit1)*int(digit2)
    print("La multiplicacion de los valores dados: "+str(multiplicacion))
    print("Desea guardar el resultado de la multiplicacion?")
    ingrese=int(input("Si(1) o No(0)?"))
    if ingrese==1:
        archivo=open("CLI2.txt","a")
        archivo.write("El valor de la multiplicacion de los valores "+digit1+" y "+digit2 +" es: "+str(multiplicacion))
        print("Se han guardado los datos correctamente")
        archivo.close()
    elif ingrese==0:
        print("Ok no se guardaran los datos")
    else:
        print("Se ha ingresado un valor invalido")
def division():
    valor_1=libreria.validar_numero(input("Ingrese el primer valor: "))
    valor_2=libreria.validar_numero(input("Ingrese  el segundo valor: "))
    division=int(valor_1)/int(valor_2)
    print("La division de los valores dados es: "+str(division))
    print("Desea guardar el resultado de la division?")
    ingrese=int(input("Si(1) o No(0)?"))
    if ingrese==1:
        archivo=open("CLI2.txt","a")
        archivo.write("EL valor de la division de los valores "+valor_1+" y "+valor_2+" es:"+str(division))
        archivo.close()
    elif ingrese==0:
        print("OK no se guardaran los datos")
    else:
        print("Se ha ingresado un valor invalido")
#importacion de la libreria
import libreria

# asig asignacion de variables int
opc=0
max=5
while opc!=max: #se asigna la funcion mientras la opc se adiferente del max seguira en el bucle
    print("################CALCULADORA#################")
    print("#1. Suma:suma 2 numeros                    #")
    print("#2. Resta:resta 2 numeros                  #")
    print("#3. Multiplicaion: multiplica 2 numeros    #")
    print("#4. Division: divide 2 numeros             #")
    print("#5. SALIR                                  #")
    print("############################################")

    #se asigna la variable opcion la cual sera llamada desde la libreria para su validacion
    opc = libreria.validar_int(input("ingrese un valor"))
    #se seleccionara la funcion segun la opcion elejida
    if opc==1:
        suma()
    if opc==2:
        resta()
    if opc==3:
        multiplicacion()
    if opc==4:
        division()
