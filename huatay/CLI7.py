def nombre_apellidos():
    nombre_apellidos=libreria.validar_apellido(input("Ingrese su nombre y apellidos"))
    archivo=open(nombre_apellidos+".txt","w")
    archivo.write("INCRIPCION"+"\n"+"NOMBRE Y APELLIDOS: "+nombre_apellidos)
    print("DATO GUARDADO CORRECTAMENTE")
    archivo.close()
def procedencia():
    nombre_apellidos = libreria.validar_apellido(input("Ingrese su nombre y apellidos"))
    escuela=libreria.validar_apellido(input("Ingrese su escuela de procedencia"))
    archivo = open(nombre_apellidos + ".txt", "a")
    archivo.write("\n"+"ESCUELA DE PROCEDENCIA: " + escuela)
    print("DATO GUARDADO CORRECTAMENTE")
    archivo.close()

def carrera_pro():
    nombre_apellidos=libreria.validar_apellido(input("Ingrese su nombre y apellidos"))
    escuela_profesional=libreria.validar_apellido(input("Ingrese su escuela profesional"))
    archivo = open(nombre_apellidos + ".txt", "a")
    archivo.write("\n"+"ESCUELA PROFESIONAL: " +escuela_profesional )
    print("DATO GUARDADO CORRECTAMENTE")
    archivo.close()
def edad():
    nombre_apellidos=libreria.validar_apellido(input("Ingrese su nombre y apellidos"))
    edad=libreria.validar_edad(input("Ingrese su edad"))
    archivo = open(nombre_apellidos + ".txt", "a")
    archivo.write("\n"+"EDAD: " + edad)
    print("DATO GUARDADO CORRECTAMENTE")
    archivo.close()
def dni():
    nombre_apellidos=libreria.validar_apellido(input("Ingrese su nombre y apellidos"))
    dni=libreria.validar_dni(input("Ingrese su DNI"))
    archivo = open(nombre_apellidos + ".txt", "a")
    archivo.write("\n"+"DNI: " + dni)
    print("DATO GUARDADO CORRECTAMENTE")
    archivo.close()

import libreria
opc=0
max=6
while opc!=max:
    print("####################INSCRIPCION######################")
    print("#1.NOMBRE Y APELLIDOS                               #")
    print("#2.ESCUELA DE PROCEDENCIA                           #")
    print("#3.CARRERA PROFESIONAL                              #")
    print("#4.EDAD                                             #")
    print("#5.DNI                                              #")
    print("#6.SALIR                                            #")
    print("#####################################################")
    print("INRESA CADA OPCION EN ORDEN PARA GENERAR SU INSCRIPCION")
    print("nota:ingrese el mismo nombre varias veces cualquier alteracion hara un fallo en el programa")
    opc=libreria.validar_eleccion(input("Ingrese su Opcion: "))

    if opc==1:
        nombre_apellidos()
    if opc==2:
        procedencia()
    if opc==3:
        carrera_pro()
    if opc==4:
        edad()
    if opc==5:
        dni()

