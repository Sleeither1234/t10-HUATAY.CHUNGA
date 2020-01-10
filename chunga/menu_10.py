import libreria

def arroz_con_pato():
    print("Disfrute su Arroz con pato")
def pollo():
    print("Disfrute su Pollo con salsa de Champiñones")
def arroz_con_mariscos():
    print("Disfrute su Arroz con mariscos")

opc=0
max=4
while opc != max:
    print("###  Restaurante Karla ###############")
    print("# 1.-- Arroz con pato   ##############")
    print("# 2.-- Pollo con salsa de Champ. #####")
    print("# 3.-- Arroz con mariscos ############")
    print("# 4.-- SALIR           ###############")
    print("######################################")
    opc = libreria.pedir_numero("¿Que desea de comer?:",1,4)
    if opc ==1:
        arroz_con_pato()
    if opc ==2:
        pollo()
    if opc ==3:
        arroz_con_mariscos()
print("Disfrute su comida")
