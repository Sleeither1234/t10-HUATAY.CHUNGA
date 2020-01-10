import libreria

opc=0
max=3
while opc != max:
    print("#########  #########")
    print("# 1.----------  ######")
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
