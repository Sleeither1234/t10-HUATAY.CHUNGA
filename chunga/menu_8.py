import libreria

def funcion_leche():
    print("Gracias por comprar Leche")

def funcion_yogurt():
    print("Gracias por comprar Yogurt")

def funcion_mantequilla():
    print("Gracias por comprar Mantequilla")

opc=0
max=4
while opc != max:
    print("############ LACTEOS ###########")
    print("# 1.--------- LECHE       ######")
    print("# 2.--------- YOGUT       ######")
    print("# 3.--------- MANTEQUILLA ######")
    print("# 4.--------- SALIR       ######")
    print("################################")
    opc = libreria.pedir_numero("¿Que desea comprar?:",1,4)
    if opc ==1:
        funcion_leche()
    if opc ==2:
        funcion_yogurt()
    if opc ==3:
        funcion_mantequilla()
print("Gracias por sus compras")
