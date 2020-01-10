import libreria
def funcion_Z():
    print("ZEUS: Hijo de cronos, rey del cielo, planeo en contra de su padre para liberar a sus hermanos.")

def funcion_H():
    print("HADES: Hijo mayor de Cronos, Rey del inframundo, posee el casco de la invisibilidad. ")

def funcion_P():
    print("POSEIDON: Hijo de Cronos, Rey del Mar y posee el tridente. ")

opc = 0
max = 4

while opc != max:
    print("######### DIOSES #########")
    print("# 1.---------- ZEUS ######")
    print("# 2.--------- HADES ######")
    print("# 3.-------POSEIDÒN ######")
    print("# 4.----------SALIR ######")
    print("##########################")
    opc = libreria.pedir_numero("Sobre que Dios busca informacion?",1,4)
    if opc ==1:
        funcion_Z()
    if opc ==2:
        funcion_H()
    if opc ==3:
        funcion_P()
print("Gracias por venir.")
