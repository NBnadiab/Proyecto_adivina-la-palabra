import random

def palabras_aleatoria():
    palabras=["caballo","elefante","mariposa","hipopotamo","oso","cocodrilo"]
    palabra_aleatoria = random.choice(palabras)
    return palabra_aleatoria


print(":::::::::::::::::::::: ADIVINA LA PALABRA :::::::::::::::::::::: ")

name=input("Hola! Por favor ingrese su nombre: ")
print(f"¡¡BIENVENIDO/A {name.upper()}!! \n\n ¿Estás listo/a para jugar?")

respuesta=input("\n Respuesta SI o NO: ")
if respuesta.upper() == "SI":
    print("\n\nTendras que escribir las letras para adivinar la palabra.")
    print("Tienes 5 vidas, si la letra es incorrecta, se descontaran vidas.")
    print("MUCHA SUERTE!!")
else:
    print("¡No hay problema! ¡Te esperamos en otro momento!")
