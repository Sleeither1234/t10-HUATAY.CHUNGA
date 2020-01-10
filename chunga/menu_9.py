import libreria
def funcion_ps4():
    print("Usted voto por la consola Play Station 4")

def funcion_xbox():
    print("Usted voto por la consola Xbox")

def funcion_wiiU():
    print("Usted voto por la consola Wii U")

opc=0
max=4
while opc != max:
    print("#######   CONSOLAS   ######")
    print("# 1.--------- PS4    ######")
    print("# 2.--------- XBOX   ######")
    print("# 3.--------- WII U  ######")
    print("# 4.--------- SALIR  ######")
    print("###########################")
    opc = libreria.pedir_numero("¿Por que consola votará?:",1,4)
    if opc ==1:
        funcion_ps4()
    if opc ==2:
        funcion_xbox()
    if opc ==3:
        funcion_wiiU()

print("Gracias por votar")
