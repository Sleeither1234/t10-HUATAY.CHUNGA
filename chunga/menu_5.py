import libreria
def funcion_mayor():
    print("Permiso consedido.")

def funcion_menor():
    print("Permiso denegado.")

opc=0
max=3
while opc != max:
    print("#### OPCIONES ####")
    print("# 1.  18 o màs ###")
    print("# 2. -18       ###")
    print("# 3.  Salir    ###")
    print("################")
    opc=libreria.pedir_numero("¿Que edad tiene?",1,3)
    if opc == 1:
        funcion_mayor()

    if opc == 2:
        funcion_menor()

print("Vuelva pronto")
