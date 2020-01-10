#ejercicio 01
def validar_entero(opc):
    if opc.isdigit()==True:
        if int(opc)<=1==False and int(opc)>4==False:
            return False
        else:
            return int(opc)
    else:
        return False
#fin_def


#ejercicio 02
def validar_int(opc):
    if opc.isdigit()==True:
        validacion=int(opc)
        if validacion>0 and validacion<6:
            return int(opc)
        else:
            return False
    else:
        return False


def validar_numero(numero):
    if numero.isdigit()==True:
        return numero
    else:
        return False


def validar_menu(opc):
    if opc.isdigit()==True:
            validacion=int(opc)
            if validacion>0 and validacion<4:
                return int(opc)
            else:
                return False
    else:
        return False


def validar_telefono(tel):
    if len(tel)==9:
       if  tel[0]=="9":
           if tel.isdigit()==True:
               return tel
           else:
               return False
       else:
           return False
    else:
        return False

def validar_contacto(nombre):
    if isinstance(nombre,str):
        if nombre.isalpha()==True:
            return nombre
        else:
            return False
    else:
        return False


def validar_codigo(codigo):
    if isinstance(codigo,str):
        if codigo[0]=="+":
            if codigo[1:].isdigit()==True:
                return codigo
            else:
                return False
        else:
            return False
    else:
        return False

def validar_contacto_internacional(numero):
    if (isinstance(numero,str)):
        return numero
    else:
        return False

def validar_edad(edad):
    if edad.isdigit()==True:
        valor=int(edad)
        if valor>0 and valor<120:
            return edad
        else:
            return False
    else:
        return False


def validar_eleccion(elejir):
    if  elejir.isdigit()==True:
        valor=int(elejir)
        if valor>0 and valor<7:
            return valor
        else:
            return False
    else:
        return False
def validar_dns(elejir):
    if  elejir.isdigit()==True:
        valor=int(elejir)
        if valor>0 and valor<6:
            return valor
        else:
            return False
    else:
        return False



def validar_dni(dni):
    if len(dni)==8:
        if dni.isdigit()==True:
            return dni
        else:
            return False
    else:

        return False


def validar_apellido(apellido):
    if isinstance(apellido,str):
        if apellido.isdigit()==False:
            return apellido
        else:
            return False
    else:
        return False

def validar_comando(comando):
    if comando.upper()=="FUEGO":
        return comando.upper()
    else:
        return False



def validar_nota(nota):
    if nota.isdigit()==True:
        valor=int(nota)
        if valor>0 and valor<=20:
            return valor
        else:
            return False
    else:
        return False

def validar_suma(numero):
    if numero.isdigit()==True:
        valor = int(numero)
        return valor
    else:
        return  False

def validar_float(numero):
    if numero.isdigit()==True:
        valor = float(numero)
        return valor
    else:
        return  False