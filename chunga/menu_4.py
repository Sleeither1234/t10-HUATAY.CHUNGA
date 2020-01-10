import libreria
def funcion_H():
    print("Gracias pasar a recoger su hamburguesa.")

def funcion_P():
    print("Gracias pasar a recoger sus Papitas.")

def funcion_K():
    print("Gracias pasar a recoger su Keke.")

opc=0
max=4
while opc != max :
    print("##### PUESTO STTEGG #####")
    print(" 1.    Hamburguesa")
    print(" 2.    Papitas    ")
    print(" 3.    Keke       ")
    print(" 4.    Salir      ")
    print("##########################")

    opc= libreria.pedir_numero("Cual serà su pedido",1,4)
    if opc == 1:
        funcion_H()

    if opc == 2:
        funcion_P()

    if opc == 3:
        funcion_K()

print("Gracias por su preferencia.")
