import libreria
def funcion_pera():
    print("se selecciono la fruta pera")

def funcion_manzana():
    print("se selecciono la fruta manzana")


def funcion_frutas():
    opc=0 #   Par ainicar el buscle
    max=3  #  PAra finalizar el bucle
    while opc!=max:
        print("########## MENU ############")
        print("#1. pera")
        print("#2. manzana")
        print("3.salir")
        print("############################")
        opc=libreria.pedir_numero("seleccione una opcion",1,3)
        if opc==1:
            funcion_pera()


# los rangos del bucle
opc=0 #   Par ainicar el buscle
max=2 #  PAra finalizar el bucle
while opc != max: # Mientras opc y max sean diferentes entrara el bucle
    print("########## MENU ############")
    print("#1. frutas")
    print("#2. salir")
    print("############################")
    opc=libreria.pedir_numero("seleccione una opcion",1,2)
    if opc==1:
        funcion_frutas()
print("Fin del programa")



