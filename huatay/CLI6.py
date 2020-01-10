def servidor():
    dns="1)8.8.8.8"
    dns1="2)9.9.9.9"
    dns2="3)1.1.1.1"
    dns3="4)1.1.0.0"
    dns4="5)8.8.4.4"
    lista=[dns,dns1,dns2,dns3,dns4]
    print( "Estos son los siguientes servidores")
    print(lista)
    nombre=libreria.validar_contacto(input("Ingrese su primer nombre: "))
    elejir_dns=libreria.validar_dns(input("Ingrese el numero del dns para ser seleccionado"))
    if elejir_dns==1:
        archivo=open("dns.txt","w")
        archivo.write("DNS: "+dns+"\n"+"USER: "+nombre+".ing"+"\n"+"PASARROW: "+nombre+"."+dns )
        print("los datos se han guardado correctamente")
        archivo.close()
    elif elejir_dns==2:
        archivo = open("dns.txt", "w")
        archivo.write("DNS: " + dns1 + "\n" + "USER: " + nombre + ".ing" + "\n" + "PASARROW: " + nombre +"."+ dns1)
        print("los datos se han guardado correctamente")
        archivo.close()
    elif elejir_dns==3:
        archivo = open("dns.txt", "w")
        archivo.write("DNS: " + dns2 + "\n" + "USER: " + nombre + ".ing" + "\n" + "PASARROW: " + nombre +"."+dns2)
        print("los datos se han guardado correctamente")
        archivo.close()
    elif elejir_dns==4:
        archivo = open("dns.txt", "w")
        archivo.write("DNS: " + dns3 + "\n" + "USER: " + nombre + ".ing" + "\n" + "PASARROW: " + nombre + "."+dns3)
        print("los datos se han guardado correctamente")
        archivo.close()
    elif elejir_dns==5:
        archivo = open("dns.txt", "w")
        archivo.write("DNS: " + dns4 + "\n" + "USER: " + nombre + ".ing" + "\n" + "PASARROW: " + nombre + "."+dns4)
        print("los datos se han guardado correctamente")
        archivo.close()
    else:
        print("Ha seleccionado valors incorrectos")
def verificador_ping():
    dns = "1)8.8.8.8"
    dns1 = "2)9.9.9.9"
    dns2 = "3)1.1.1.1"
    dns3 = "4)1.1.0.0"
    dns4 = "5)8.8.4.4"
    lista = [dns, dns1, dns2, dns3, dns4]
    print("Estos son los siguientes servidores")
    print(lista)
    nombre = libreria.validar_contacto(input("Ingrese su nombre: "))
    elejir_dns = libreria.validar_dns(input("Ingrese el numero del dns para ser seleccionado"))
    if elejir_dns == 1:
        archivo = open("dns.txt", "a")
        ping=44
        if ping>0 and ping<100:
            print("Su conexion es buena y no hay perdida de paqueta")
        elif ping>100 and ping<1000:
            print("Su coneccion es un poco inestable perdida de paquete 25%")
        elif ping>1000:
            print("perdida de paquetes al 75% sevidor agotado")
        archivo.write( "\n" +"PING: "+str(ping)+"ms" )
        print("los datos se han guardado correctamente")
        archivo.close()
    elif elejir_dns == 2:
        archivo = open("dns.txt", "a")
        ping = 123
        if ping > 0 and ping < 100:
            print("Su conexion es buena y no hay perdida de paqueta")
        elif ping > 100 and ping < 1000:
            print("Su coneccion es un poco inestable perdida de paquete 25%")
        elif ping > 1000:
            print("perdida de paquetes al 75% sevidor agotado")
        archivo.write( "\n" + "PING: " + str(ping)+"ms")
        print("los datos se han guardado correctamente")
        archivo.close()
    elif elejir_dns == 3:
        archivo = open("dns.txt", "a")
        ping = 234
        if ping > 0 and ping < 100:
            print("Su conexion es buena y no hay perdida de paqueta")
        elif ping > 100 and ping < 1000:
            print("Su coneccion es un poco inestable perdida de paquete 25%")
        elif ping > 1000:
            print("perdida de paquetes al 75% sevidor agotado")
        archivo.write("DNS: " + dns2 + "\n" + "PING: " + str(ping)+"ms")
        print("los datos se han guardado correctamente")
        archivo.close()
    elif elejir_dns == 4:
        archivo = open("dns.txt", "a")
        ping = 1111
        if ping > 0 and ping < 100:
            print("Su conexion es buena y no hay perdida de paqueta")
        elif ping > 100 and ping < 1000:
            print("Su coneccion es un poco inestable perdida de paquete 25%")
        elif ping > 1000:
            print("perdida de paquetes al 75% sevidor agotado")
        archivo.write( "\n" + "PING: " + str(ping)+"ms")
        print("los datos se han guardado correctamente")
        archivo.close()
    elif elejir_dns == 5:
        archivo = open("dns.txt", "a")
        ping = 42112
        if ping > 0 and ping < 100:
            print("Su conexion es buena y no hay perdida de paqueta")
        elif ping > 100 and ping < 1000:
            print("Su coneccion es un poco inestable perdida de paquete 25%")
        elif ping > 1000:
            print("perdida de paquetes al 75% sevidor agotado")
        archivo.write( "\n" + "PING: " + str(ping)+"ms")
        print("los datos se han guardado correctamente")
        archivo.close()
    else:
        print("Ha seleccionado valors incorrectos")


import libreria
opc=0
max=3
while opc!=max:
    print("################SEÑAL###########################")
    print("#1.SERVIDORES  (ingrese cada opcion en orden)  #")
    print("#2.VERIFICAION DE MI PING Y SU ESTADO          #")
    print("#3.SALIR                                       #")
    print("################################################")
    opc=libreria.validar_menu(input("Ingrese su opcion: "))
    if opc==1:
        servidor()
    if opc==2:
        verificador_ping()
