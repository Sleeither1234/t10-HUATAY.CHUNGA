def llamar():
    def hacer_llamada():
        numero=libreria.validar_telefono(input("INGRESE EL NUMERO TELEFONICO POR FAVOR "))
        print("MARCANDO al "+numero)


    def agregar_contacto():
        agregar=libreria.validar_apellido(input("INGRESE EL NOMBRE DEL CONTACTO QUE DESEA AGREGAR"))
        numero=libreria.validar_telefono(input("Ingrese el numero telefonico "))
        lista=[agregar,numero]
        archivar_contacto=open("libreta.txt","a")
        archivar_contacto.write("CONTACTO"+"\n"+"contacto,numero "+str(lista))
        print("Archivo guardado correctamente")
        archivar_contacto.close()
    opc=0
    max=3
    while opc!=3:
        print("#########LLAMAR##########")
        print("#1.Hacer llamada        #")
        print("#2.Agregar contacto     #")
        print("#3.salir                #")
        print("#########################")
        opc=libreria.validar_menu(input("Ingrese su opcion "))
        if opc==1:
            hacer_llamada()
        if opc==2:
            agregar_contacto()
def mensaje():
    def enviar():
        numero=libreria.validar_telefono(input("Ingrese el numero al que desea enviar mensaje "))
        mensaje=input("Ingrese su mensaje que desea enviar")
        lista=[numero,mensaje]
        archivo=open(numero+".txt","w")
        archivo.write(mensaje)
        print("mensaje enviado")
        archivo.close()

        print("Mensaje enviado correctamente")
        archivo.close()
    def eliminar():
        numero = libreria.validar_telefono(input("Ingrese el numero al que desea enviar mensaje "))
        mensaje = input("Ingrese su mensaje que desea enviar")
        lista = [numero, mensaje]
        archivo = open(numero + ".txt", "w")
        archivo.write(mensaje)
        print("mensaje enviado")
        eliminar=int(input("DESEA ELIMINAR EL SIGUIENTE MENSAJE? SI(1)O NO(0)"))
        if eliminar==1:
            lista.clear()
            del lista[:]
            print("Mensaje eliminado")
        if eliminar==0:
            print("Ok no se eliminara el mensaje")
        else:
            print("COMANDO INVALIDO")
        archivo.close()
    opc=0
    max=3
    while opc!=max:
        print("########MENSAJE############")
        print("#1.ENVIAR MENSAJE         #")
        print("#2.ELIMINAR MENSAJE       #")
        print("#3.salir                  #")
        print("###########################")
        opc=libreria.validar_menu(input("Ingrese su opcion "))
        if opc==1:
            enviar()
        if opc==2:
            eliminar()
import libreria
opc=0
max=3
while opc!=max:
    print("#######MENSAJES Y LLAMADAS#######")
    print("#1.LLAMAR                       #")
    print("#2.MENSAJES                     #")
    print("#3.salir                        #")
    print("#################################")
    opc=libreria.validar_menu(input("Ingrese su opcion"))
    if opc==1:
        llamar()
    if opc==2:
        mensaje()
