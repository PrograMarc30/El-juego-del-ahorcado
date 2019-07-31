from random import *
partida = True
while True:
    if partida == True:
        nombre = input("Hola, ¿cómo te llamas?: ")
        print("")
        print("******************************************************")
        print("")
        print(nombre,", estoy pensando en un número entre el 1 y el 100")
        print("")
        print("")
        intentos = 0
        vidas = 6
        numero = randint (1,100)
        while intentos < 6 :
            print("tienes ",vidas," intentos")
            estimacion = int (input("                              intenta adivinar: "))
            print("")
            intentos = intentos + 1
            vidas = vidas - 1
            if estimacion < numero :
                print("tu estimación es muy baja")
            elif estimacion > numero :
                print("tu estimación es muy alta")
            elif estimacion == numero:
                break
        if numero == estimacion :
            print("Buen trabajo ",nombre,", has adivinado el número en ",intentos,"intentos")
            nuevapartida = input("Quieres empezar una nueva partida??? (y/n):  ")
            if nuevapartida == "y":
                partida = True
            elif nuevapartida == "n":
                break
        elif numero != estimacion:
            print("perdiste ",nombre,", el número que estaba pensando es el ",numero)
            nuevapartida = input("Quieres empezar una nueva partida??? (y/n):  ")
            if nuevapartida == "y":
                partida = True
            elif nuevapartida == "n":
                break