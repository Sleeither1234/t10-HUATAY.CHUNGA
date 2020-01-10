def validar_entero(n):
    if (isinstance(n,int)): # Pregunta si el numero ingresado(n) es un entero
        return True      # Si cumple retorna True
    else:
        return False     # De no ser un entero retornara False


def validar_rango(n, ri, rf): # Se le envia el numero con el rango (ri,rf) rango inical y final respectiamente
    if ( validar_entero(n) == True): # Si cumple el validar_entero entonces:
                                     # Empezara a validar si esta dentro del rango
        if ( n >= ri and n<= rf):    # El numero debe ser mayor igual que ri y menor igual que rf
            return True  # Si cumple retorna True
        else:
            return False # Sino retorna False
    else:
        return False # De no cumplirse validar_entero retorna False



def pedir_numero(msg, ri, rf):  # Los parametros seran el mensaje rango inicial
                                #                y el rango final
    n=""   # n es nuesta cadena vacia
    while ( validar_rango(n, ri, rf) == False): # Mientas validar rango sea falso:
        n=input(msg)                            # Pedira ingresar el valor a n
        if (n.isdigit() == True):               # Se pregunta si la cadena posee digitos:
            n=int(n)                            # Si es asì lo convertiremos a entero

    #fin while
    return n                                    # Si validar rango es verdadero retorna el valor de n
#fin_pedir_numero



def guardar_datos(nombre_archivo,contenido,modo):
    archivo=open(nombre_archivo,modo)
    archivo.write(contenido)
    archivo.close()

def obtener_datos(nombre_archivo):
    archivo=open(nombre_archivo)
    contenido=archivo.read()
    archivo.close()
    return contenido


