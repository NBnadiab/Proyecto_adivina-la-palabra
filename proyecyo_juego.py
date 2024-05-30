import random

def palabras_aleatoria():
    palabras=["caballo","elefante","mariposa","hipopotamo","oso","cocodrilo"]
    palabra_aleatoria = random.choice(palabras)
    return palabra_aleatoria

def mostrar_guiones(palabra_secreta, letras_adivinadas):
    tablero=" "

    for letra in palabra_secreta:
        if letra in letras_adivinadas:
            tablero+=letra
        else:
            tablero+="_ "
            
    print(f"\n\n{tablero}")         
         

def juego():
     palabra_secreta=palabras_aleatoria()
     letras_adivinadas=[]
     vidas = 5
     letras_usadas=[]

     while vidas>0:
         mostrar_guiones(palabra_secreta, letras_adivinadas)
         letra=input("\nIntruduce una letra: ").lower()   
            
         
         if letra in letras_adivinadas:
             print("\nYa adivinaste esa letra, ¡Intente otra!")
         else: 
             letras_usadas.append(letra)
             print(f"Letras usadas: {letras_usadas}")
             
         if letra in palabra_secreta:
           letras_adivinadas.append(letra)
           if set(letras_adivinadas) == set(palabra_secreta):
               print(f"\nLa palabra es: {palabra_secreta.upper()}")
               print(f"\n¡¡FELICITACIONES!! Has ganado!!")

               break
           
         else:
             vidas-=1
             print(f"\nLetra incorrecta. Te quedan: {vidas} vidas")

         if vidas==0:
          print(f"\nHas perdido. La palabra es: {palabra_secreta.upper()}")
          

print(":::::::::::::::::::::: ADIVINA LA PALABRA :::::::::::::::::::::: ")

name=input("\nHola! Por favor ingrese su nombre: ")
print(f"¡¡BIENVENIDO/A {name.upper()}!! \n\n ¿Estás listo/a para jugar?")

respuesta=input("\n Respuesta SI o NO: ")
if respuesta.upper() == "SI":
    print("\nTendras que escribir las letras para adivinar la palabra.")
    print("Tienes 5 vidas, si la letra es incorrecta, se descontaran vidas.")
    print("\nMUCHA SUERTE!!")
else:
    print("\n¡No hay problema! ¡Te esperamos en otro momento!")
    
    
juego()
