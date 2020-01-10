import  libreria    #Hacemos llamado a la libreria
def notaP():        # Creamos la funcion para la opcion "programacion"
    print("20")     # Enviamos el resultado de la funcion

def notaM():        # Creamos la funcion para la opcion "Mate basica"
    print("12")     # Enviamos el resultado de la funcion

def notaA():        # Creamos la funcion para la opcion "Analisis Matematico"
    print("14")     # Enviamos el resultado de la funcion

def notaT():        # Creamos la funcion para la opcion "Tecnicas de estudio"
    print("17")     # Enviamos el resultado de la funcion

opc = 0             # Varible para inciar el bucle
max = 5             # Variable para finalizar el bucle
while opc != max:   # Se condiciona el bucle con las variables
    # Imprimimos el menu
    print("###### NOTA DE CUROS ######")
    print(" 1. PROGRAMACION     ######")
    print(" 2. MATE BASICA      ######")
    print(" 3. ANALISIS MATEMATICO ###")
    print(" 4. TECNICAS DE ESTUDIO ###")
    print(" 5. SALIR            ######")
    opc= libreria.pedir_numero("Ingrese su opcion:",1,5)
    if opc == 1:
        notaP()
    if opc == 2:
        notaM()
    if opc == 3:
        notaA()
    if opc == 4:
        notaT()
print("GRACIAS.")
