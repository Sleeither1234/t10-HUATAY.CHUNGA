def calculo():
        nombre=libreria.validar_apellido(input("INGRESE EL NOMBRE DEL ALUMNO"))
        nota1=libreria.validar_nota(input("INGRESE LA NOTA 1"))
        nota2=libreria.validar_nota(input("INGRESE LA NOTA 2"))
        nota3=libreria.validar_nota(input("INGRESE LA NOTA 3"))
        nota4=libreria.validar_nota(input("INGRESE LA NOTA 4"))
        promedio=(nota1+nota2+nota3+nota4)/4
        print("El promedio es: "+str(promedio))
        archivo=open(nombre+".txt","w")
        archivo.write("\t"+"REGISTRO"+"\n"+"NOMBRE: "+nombre+"\n"+"NOTA 1: "+str(nota1)+"\n"+"NOTA 2: "+str(nota2)+"\n"+"NOTA 3: "+str(nota3)+"\n"+"NOTA 4: "+str(nota4)+"\n"+"PROMEDIO FINAL: "+str(promedio))
        print("REGISTRO DE ALUMNO GENERADO")
        archivo.close()

def comprobacion_alumnos():
    nombre = libreria.validar_apellido(input("INGRESE EL NOMBRE DEL ALUMNO"))
    nota1 = libreria.validar_nota(input("INGRESE LA NOTA 1"))
    nota2 = libreria.validar_nota(input("INGRESE LA NOTA 2"))
    nota3 = libreria.validar_nota(input("INGRESE LA NOTA 3"))
    nota4 = libreria.validar_nota(input("INGRESE LA NOTA 4"))
    promedio = (nota1 + nota2 + nota3 + nota4) / 4
    print("El promedio es: " + str(promedio))
    if promedio>10.5:
        archivo = open(nombre + ".txt", "w")
        archivo.write(
            "\t" + "REGISTRO" + "\n" + "NOMBRE: " + nombre + "\n" + "NOTA 1: " + str(nota1) + "\n" + "NOTA 2: " + str(
                nota2) + "\n" + "NOTA 3: " + str(nota3) + "\n" + "NOTA 4: " + str(
                nota4) + "\n" + "PROMEDIO FINAL: " + str(promedio)+"\n"+"EL ALUMNO"+nombre+" esta aprobado")
        print("REGISTRO DE ALUMNO GENERADO")
        archivo.close()
    else:
        archivo = open(nombre + ".txt", "w")
        archivo.write(
            "\t" + "REGISTRO" + "\n" + "NOMBRE: " + nombre + "\n" + "NOTA 1: " + str(nota1) + "\n" + "NOTA 2: " + str(
                nota2) + "\n" + "NOTA 3: " + str(nota3) + "\n" + "NOTA 4: " + str(
                nota4) + "\n" + "PROMEDIO FINAL: " + str(promedio)+"\n"+"El ALUMNO  "+nombre+" ESTA DESAPROBADO")
        print("REGISTRO DE ALUMNO GENERADO")
        archivo.close()
import  libreria
opc=0
max=3
while opc!=max:
    print("###############NOTAS DE ALUMNOS##########")
    print("#1.REGISTRO DE NOTAS DEL ALUMNO         #")
    print("2.COMPROBACION DE ALUMNOS APROBADOS     #")
    print("#3.SALIR                                #")
    print("#########################################")
    opc=libreria.validar_menu(input("Ingrese su opcion "))
    print("POR RECOMENDACION UTILIZE LAS OPCIONES EN ORDEN :)")
    if opc==1:
        calculo()
    if opc==2:
        comprobacion_alumnos()
